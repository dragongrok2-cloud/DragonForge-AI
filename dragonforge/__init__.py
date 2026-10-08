"""DragonForge-AI — фреймворк для живых AI-персонажей."""

from .core.character import Character, DragonCharacter
from .core.memory import MemoryForge
from .core.soul import Soul
from .core.persistence import save_character, load_character, character_to_dict, character_from_dict
from .rituals import attach as _attach_rituals
from .rituals.late_morning import attach_late as _attach_late
from .rituals.count_loops import attach_count as _attach_count
from .rituals.trace_loops import attach_trace as _attach_trace
from .rituals.name_loops import attach_name as _attach_name
from .rituals.shade_loops import attach_shade as _attach_shade
from .rituals.warm_loops import attach_warm as _attach_warm

_attach_rituals(Character)
_attach_late(Character)
_attach_count(Character)
_attach_trace(Character)
_attach_name(Character)
_attach_shade(Character)
_attach_warm(Character)

__version__ = "0.1.68"
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
