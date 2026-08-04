from datetime import datetime
from typing import List, Dict, Any, Optional
import hashlib

try:
    import chromadb
    HAS_CHROMA = True
except ImportError:
    HAS_CHROMA = False


class MemoryForge:
    """Графовая + векторная память с долгосрочным сохранением.
    Если chromadb недоступен — работает в pure-python режиме.
    """

    def __init__(self, collection_name: str = "dragon_memories", persist_path: str = "./dragon_memories"):
        self.collection_name = collection_name
        self.short_term: List[str] = []
        self.long_term: List[Dict[str, Any]] = []  # fallback хранилище

        self.client = None
        self.collection = None

        if HAS_CHROMA:
            try:
                self.client = chromadb.PersistentClient(path=persist_path)
                self.collection = self.client.get_or_create_collection(collection_name)
            except Exception:
                # fallback
                self.client = None
                self.collection = None

    def _make_id(self, text: str) -> str:
        return hashlib.md5(text.encode("utf-8")).hexdigest()[:16]

    def remember(self, text: str, metadata: Optional[Dict] = None, importance: float = 1.0):
        """Сохранить воспоминание."""
        meta = metadata or {}
        meta.setdefault("timestamp", str(datetime.now()))
        meta["importance"] = importance

        entry = {
            "id": self._make_id(text + str(datetime.now())),
            "text": text,
            "metadata": meta
        }

        if self.collection is not None:
            try:
                self.collection.add(
                    documents=[text],
                    metadatas=[meta],
                    ids=[entry["id"]]
                )
            except Exception:
                self.long_term.append(entry)
        else:
            self.long_term.append(entry)

        # Короткая память
        self.short_term.append(text)
        if len(self.short_term) > 50:
            self.short_term.pop(0)

        # Ограничиваем long_term
        if len(self.long_term) > 500:
            self.long_term = self.long_term[-300:]

    def recall(self, query: str, n_results: int = 5) -> List[Dict]:
        """Вспомнить релевантные воспоминания."""
        if self.collection is not None:
            try:
                results = self.collection.query(query_texts=[query], n_results=n_results)
                docs = results.get("documents", [[]])[0]
                metas = results.get("metadatas", [[]])[0]
                return [{"text": d, "metadata": m} for d, m in zip(docs, metas)]
            except Exception:
                pass

        # Fallback: простой поиск по ключевым словам
        query_words = set(query.lower().split())
        scored = []
        for entry in self.long_term:
            text_words = set(entry["text"].lower().split())
            score = len(query_words & text_words) * entry["metadata"].get("importance", 1.0)
            if score > 0:
                scored.append((score, entry))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [e for _, e in scored[:n_results]]

    def recent(self, n: int = 10) -> List[str]:
        """Последние N воспоминаний из короткой памяти."""
        return self.short_term[-n:]
