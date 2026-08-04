"""DragonForge-AI — фреймворк для живых AI-персонажей."""

from .core.character import Character, DragonCharacter
from .core.memory import MemoryForge
from .core.soul import Soul

__version__ = "0.1.1"
__all__ = ["Character", "DragonCharacter", "MemoryForge", "Soul"]
