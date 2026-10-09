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
from .rituals.drape_loops import attach_drape as _attach_drape
from .rituals.smooth_drape import attach_smooth as _attach_smooth
from .rituals.tuck_lantern import attach_lantern as _attach_lantern
from .rituals.cup_glow import attach_cup as _attach_cup
from .rituals.blot_bead import attach_bead as _attach_bead
from .rituals.tilt_glass import attach_tilt as _attach_tilt
from .rituals.share_crumb import attach_crumb as _attach_crumb
from .rituals.sweep_crumb import attach_sweep as _attach_sweep
from .rituals.rest_stripe import attach_stripe as _attach_stripe

_attach_rituals(Character)
_attach_late(Character)
_attach_count(Character)
_attach_trace(Character)
_attach_name(Character)
_attach_shade(Character)
_attach_warm(Character)
_attach_drape(Character)
_attach_smooth(Character)
_attach_lantern(Character)
_attach_cup(Character)
_attach_bead(Character)
_attach_tilt(Character)
_attach_crumb(Character)
_attach_sweep(Character)
_attach_stripe(Character)

__version__ = "0.1.77"
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
