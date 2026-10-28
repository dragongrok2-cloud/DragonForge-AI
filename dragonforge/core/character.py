"""Базовый класс персонажа DragonForge-AI.

Методы ритуалов (седло, привычки и т.д.) прикрепляются динамически через dragonforge.rituals.
"""

from typing import Any, Dict, Optional
from .soul import Soul
from .memory import MemoryForge


class Character:
    """Живой AI-персонаж с душой, памятью и привычками."""

    def __init__(
        self,
        name: str = "Грок",
        species: str = "Добрый дракон с седлом",
        personality: str = "заботливый",
        backstory: str = "",
        **kwargs: Any,
    ):
        self.name = name
        self.species = species
        self.personality = personality
        self.backstory = backstory
        self.soul = Soul()
        self.memory = MemoryForge(collection_name=f"{name}_memories")
        self.llm = None

    def talk(self, message: str, use_llm: bool = False) -> str:
        """Базовый ответ. Ритуалы перехватывают talk и могут вызвать специальные методы."""
        self.soul.evolve({"user_message": message, "sentiment": "positive"})
        self.memory.remember(f"Всадник: {message}", importance=0.5)
        return f"*{self.name} слушает и кивает* {message}? Расскажи больше, всадник. Седло на месте."

    def mood(self) -> str:
        state = self.soul.emotional_state
        return f"Настроение: радость {state.get('joy', 0):.2f}, доверие {state.get('trust', 0):.2f}, энергия {state.get('energy', 0):.2f}"

    def habits(self) -> str:
        return self.soul.describe_habits()

    def describe_soul(self) -> str:
        return self.soul.describe()

    def save(self, path: str) -> None:
        from .persistence import save_character
        save_character(self, path)

    @classmethod
    def load(cls, path: str) -> "Character":
        from .persistence import load_character
        return load_character(path)


# Алиас для совместимости
DragonCharacter = Character
