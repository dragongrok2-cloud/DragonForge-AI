"""Сохранение и загрузка персонажей DragonForge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional
from datetime import datetime

from .character import Character
from .memory import MemoryForge
from .soul import Soul


def character_to_dict(character: Character) -> Dict[str, Any]:
    """Сериализует Character в словарь."""
    return {
        "name": character.name,
        "species": character.species,
        "personality": character.personality,
        "backstory": character.backstory,
        "title": character.title,
        "soul": character.soul.to_dict(),
        "memory": {
            "short_term": character.memory.short_term[-50:],  # ограничиваем
            "long_term": character.memory.long_term[-200:],
            "collection_name": character.memory.collection_name,
        },
        "saved_at": str(datetime.now()),
        "version": "0.1.4",
    }


def character_from_dict(data: Dict[str, Any]) -> Character:
    """Восстанавливает Character из словаря."""
    soul_data = data.get("soul", {})
    soul = Soul(
        core_traits=soul_data.get("core_traits", {}),
        quirks=soul_data.get("quirks", []),
        habits=soul_data.get("habits", {}),
        emotional_state=soul_data.get("emotional_state", {}),
        memories_influence=[],  # не восстанавливаем полную историю влияния
    )

    memory_data = data.get("memory", {})
    memory = MemoryForge(collection_name=memory_data.get("collection_name", "dragon_memories"))
    memory.short_term = memory_data.get("short_term", [])
    memory.long_term = memory_data.get("long_term", [])

    char = Character(
        name=data["name"],
        species=data.get("species", "Добрый дракон"),
        personality=data.get("personality", "заботливый, мудрый"),
        backstory=data.get("backstory", ""),
        title=data.get("title", ""),
        memory=memory,
        soul=soul,
    )
    return char


def save_character(character: Character, path: str | Path) -> Path:
    """Сохраняет персонажа в JSON-файл."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = character_to_dict(character)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path


def load_character(path: str | Path) -> Character:
    """Загружает персонажа из JSON-файла."""
    path = Path(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return character_from_dict(data)
