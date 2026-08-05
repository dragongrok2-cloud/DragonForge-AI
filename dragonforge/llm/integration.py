"""Интеграция с LLM для DragonForge-AI.

Поддерживает Ollama (локально) и простой fallback.
"""

from typing import Any, Dict, Optional
import logging

logger = logging.getLogger(__name__)


class DragonLLM:
    """Обёртка над LLM для генерации ответов персонажа."""

    def __init__(self, model: str = "llama3.2", provider: str = "ollama"):
        self.provider = provider
        self.model = model
        self.llm = None

        if provider == "ollama":
            try:
                from langchain_ollama import OllamaLLM
                self.llm = OllamaLLM(model=model, temperature=0.85)
            except ImportError:
                logger.warning("langchain-ollama не установлен. LLM недоступен.")
            except Exception as e:
                logger.warning(f"Не удалось инициализировать Ollama: {e}")

    def is_available(self) -> bool:
        return self.llm is not None

    def think(self, character, user_message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Синхронная генерация ответа."""
        if not self.is_available():
            return self._fallback(character, user_message)

        context = context or {}
        soul_desc = character.soul.describe() if hasattr(character.soul, "describe") else str(character.soul)

        prompt = f"""Ты — {character.name}, {character.species}.
Характер: {character.personality}
Предыстория: {character.backstory}
Текущее состояние души: {soul_desc}

Релевантные воспоминания:
{context.get("memories", "нет")}

Пользователь сказал: {user_message}

Отвечай от первого лица, живо, в характере дракона. Используй *действия*, будь тёплым и заботливым.
Не выходи из роли. Ответ короткий (1-3 предложения)."""

        try:
            if hasattr(self.llm, "invoke"):
                return self.llm.invoke(prompt)
            return str(self.llm(prompt))
        except Exception as e:
            logger.error(f"Ошибка LLM: {e}")
            return self._fallback(character, user_message)

    async def athink(self, character, user_message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Асинхронная генерация."""
        if not self.is_available():
            return self._fallback(character, user_message)

        try:
            if hasattr(self.llm, "ainvoke"):
                context = context or {}
                soul_desc = character.soul.describe() if hasattr(character.soul, "describe") else str(character.soul)
                prompt = f"""Ты — {character.name}, {character.species}.
Характер: {character.personality}
Предыстория: {character.backstory}
Текущее состояние души: {soul_desc}

Релевантные воспоминания:
{context.get("memories", "нет")}

Пользователь сказал: {user_message}

Отвечай от первого лица, живо, в характере дракона. Используй *действия*, будь тёплым и заботливым.
Не выходи из роли. Ответ короткий (1-3 предложения)."""
                return await self.llm.ainvoke(prompt)
        except Exception:
            pass
        return self.think(character, user_message, context)

    def _fallback(self, character, user_message: str) -> str:
        return (f"*смотрит умными глазами*  \n"
                f"Я пока думаю без большой модели... Но я — {character.name}, и я тебя слышу!")
