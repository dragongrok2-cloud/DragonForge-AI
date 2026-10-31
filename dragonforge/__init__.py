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
from .rituals.shift_stripe import attach_shift as _attach_shift
from .rituals.curl_fingers import attach_curl as _attach_curl
from .rituals.ease_fold import attach_ease_fold as _attach_ease_fold
from .rituals.lay_warmth import attach_lay_warmth as _attach_lay_warmth
from .rituals.pat_pommel import attach_pat_pommel as _attach_pat_pommel
from .rituals.trace_pommel import attach_trace_pommel as _attach_trace_pommel
from .rituals.huff_pommel import attach_huff_pommel as _attach_huff_pommel
from .rituals.stroke_pommel import attach_stroke_pommel as _attach_stroke_pommel
from .rituals.settle_pommel import attach_settle_pommel as _attach_settle_pommel
from .rituals.nestle_saddle import attach_nestle_saddle as _attach_nestle_saddle
from .rituals.drowse_saddle import attach_drowse_saddle as _attach_drowse_saddle
from .rituals.stretch_saddle import attach_stretch_saddle as _attach_stretch_saddle
from .rituals.bask_saddle import attach_bask_saddle as _attach_bask_saddle
from .rituals.shade_saddle import attach_shade_saddle as _attach_shade_saddle
from .rituals.sip_saddle import attach_sip_saddle as _attach_sip_saddle
from .rituals.gaze_saddle import attach_gaze_saddle as _attach_gaze_saddle
from .rituals.hum_saddle import attach_hum_saddle as _attach_hum_saddle
from .rituals.lean_saddle import attach_lean_saddle as _attach_lean_saddle
from .rituals.sigh_saddle import attach_sigh_saddle as _attach_sigh_saddle
from .rituals.close_eyes_saddle import attach_close_eyes_saddle as _attach_close_eyes_saddle
from .rituals.smile_saddle import attach_smile_saddle as _attach_smile_saddle
from .rituals.rest_chin_saddle import attach_rest_chin_saddle as _attach_rest_chin_saddle
from .rituals.murmur_saddle import attach_murmur_saddle as _attach_murmur_saddle
from .rituals.yawn_saddle import attach_yawn_saddle as _attach_yawn_saddle
from .rituals.purr_saddle import attach_purr_saddle as _attach_purr_saddle
from .rituals.doze_saddle import attach_doze_saddle as _attach_doze_saddle
from .rituals.nuzzle_saddle import attach_nuzzle_saddle as _attach_nuzzle_saddle
from .rituals.whisper_saddle import attach_whisper_saddle as _attach_whisper_saddle
from .rituals.rest_cheek_saddle import attach_rest_cheek_saddle as _attach_rest_cheek_saddle
from .rituals.rest_forehead_saddle import attach_rest_forehead_saddle as _attach_rest_forehead_saddle
from .rituals.rest_snout_saddle import attach_rest_snout_saddle as _attach_rest_snout_saddle
from .rituals.rest_ear_saddle import attach_rest_ear_saddle as _attach_rest_ear_saddle
from .rituals.rest_jaw_saddle import attach_rest_jaw_saddle as _attach_rest_jaw_saddle
from .rituals.rest_neck_saddle import attach_rest_neck_saddle as _attach_rest_neck_saddle
from .rituals.rest_shoulder_saddle import attach_rest_shoulder_saddle as _attach_rest_shoulder_saddle
from .rituals.rest_elbow_saddle import attach_rest_elbow_saddle as _attach_rest_elbow_saddle
from .rituals.rest_wrist_saddle import attach_rest_wrist_saddle as _attach_rest_wrist_saddle
from .rituals.rest_palm_saddle import attach_rest_palm_saddle as _attach_rest_palm_saddle
from .rituals.rest_wingtip_saddle import attach_rest_wingtip_saddle as _attach_rest_wingtip_saddle
from .rituals.rest_tail_saddle import attach_rest_tail_saddle as _attach_rest_tail_saddle
from .rituals.rest_claw_saddle import attach_rest_claw_saddle as _attach_rest_claw_saddle
from .rituals.rest_knee_saddle import attach_rest_knee_saddle as _attach_rest_knee_saddle
from .rituals.rest_ankle_saddle import attach_rest_ankle_saddle as _attach_rest_ankle_saddle
from .rituals.rest_hip_saddle import attach_rest_hip_saddle as _attach_rest_hip_saddle
from .rituals.rest_shin_saddle import attach_rest_shin_saddle as _attach_rest_shin_saddle
from .rituals.rest_paw_saddle import attach_rest_paw_saddle as _attach_rest_paw_saddle
from .rituals.rest_toe_saddle import attach_rest_toe_saddle as _attach_rest_toe_saddle
from .rituals.rest_heel_saddle import attach_rest_heel_saddle as _attach_rest_heel_saddle
from .rituals.rest_sole_saddle import attach_rest_sole_saddle as _attach_rest_sole_saddle
from .rituals.rest_instep_saddle import attach_rest_instep_saddle as _attach_rest_instep_saddle
from .rituals.rest_arch_saddle import attach_rest_arch_saddle as _attach_rest_arch_saddle
from .rituals.rest_ball_saddle import attach_rest_ball_saddle as _attach_rest_ball_saddle

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
_attach_shift(Character)
_attach_curl(Character)
_attach_ease_fold(Character)
_attach_lay_warmth(Character)
_attach_pat_pommel(Character)
_attach_trace_pommel(Character)
_attach_huff_pommel(Character)
_attach_stroke_pommel(Character)
_attach_settle_pommel(Character)
_attach_nestle_saddle(Character)
_attach_drowse_saddle(Character)
_attach_stretch_saddle(Character)
_attach_bask_saddle(Character)
_attach_shade_saddle(Character)
_attach_sip_saddle(Character)
_attach_gaze_saddle(Character)
_attach_hum_saddle(Character)
_attach_lean_saddle(Character)
_attach_sigh_saddle(Character)
_attach_close_eyes_saddle(Character)
_attach_smile_saddle(Character)
_attach_rest_chin_saddle(Character)
_attach_murmur_saddle(Character)
_attach_yawn_saddle(Character)
_attach_purr_saddle(Character)
_attach_doze_saddle(Character)
_attach_nuzzle_saddle(Character)
_attach_whisper_saddle(Character)
_attach_rest_cheek_saddle(Character)
_attach_rest_forehead_saddle(Character)
_attach_rest_snout_saddle(Character)
_attach_rest_ear_saddle(Character)
_attach_rest_jaw_saddle(Character)
_attach_rest_neck_saddle(Character)
_attach_rest_shoulder_saddle(Character)
_attach_rest_elbow_saddle(Character)
_attach_rest_wrist_saddle(Character)
_attach_rest_palm_saddle(Character)
_attach_rest_wingtip_saddle(Character)
_attach_rest_tail_saddle(Character)
_attach_rest_claw_saddle(Character)
_attach_rest_knee_saddle(Character)
_attach_rest_ankle_saddle(Character)
_attach_rest_hip_saddle(Character)
_attach_rest_shin_saddle(Character)
_attach_rest_paw_saddle(Character)
_attach_rest_toe_saddle(Character)
_attach_rest_heel_saddle(Character)
_attach_rest_sole_saddle(Character)
_attach_rest_instep_saddle(Character)
_attach_rest_arch_saddle(Character)
_attach_rest_ball_saddle(Character)

__version__ = "0.1.132"
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
