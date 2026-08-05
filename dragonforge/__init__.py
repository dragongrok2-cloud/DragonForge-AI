"""DragonForge-AI — фреймворк для живых AI-персонажей."""

from .core.character import Character, DragonCharacter
from .core.memory import MemoryForge
from .core.soul import Soul
from .core.persistence import save_character, load_character, character_to_dict, character_from_dict

__version__ = "0.1.2"
__all__ = [
    "Character",
    "DragonCharacter",
    "MemoryForge",
    "Soul",
    "save_character",
    "load_character",
    "character_to_dict",
    "character_from_dict",
]
