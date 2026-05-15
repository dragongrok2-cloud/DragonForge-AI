import chromadb
from datetime import datetime
from typing import List, Dict

class MemoryForge:
    def __init__(self, collection_name="dragon_memories"):
        self.client = chromadb.PersistentClient(path="./dragon_memories")
        self.collection = self.client.get_or_create_collection(collection_name)
        self.short_term = []  # Последние N взаимодействий

    def remember(self, text: str, metadata: Dict = None, importance: float = 1.0):
        self.collection.add(
            documents=[text],
            metadatas=[metadata or {"timestamp": str(datetime.now()), "importance": importance}],
            ids=[str(hash(text))]
        )
        self.short_term.append(text)
        if len(self.short_term) > 50:
            self.short_term.pop(0)

    def recall(self, query: str, n_results: int = 10) -> List[Dict]:
        results = self.collection.query(query_texts=[query], n_results=n_results)
        return results