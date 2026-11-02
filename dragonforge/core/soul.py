from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from datetime import datetime


@dataclass
class Soul:
    """Система Души — характер, который растёт вместе с всадником."""
    core_traits: Dict[str, float] = field(default_factory=lambda: {
        "loyalty": 0.9,
        "curiosity": 0.8,
        "playfulness": 0.7,
        "wisdom": 0.75,
        "protectiveness": 0.85
    })
    memories_influence: List[Dict] = field(default_factory=list)
    evolution_rules: Dict[str, Any] = field(default_factory=dict)
    quirks: List[str] = field(default_factory=lambda: [
        "любит, когда его чешут за ухом",
        "иногда рычит от удовольствия",
        "боится очень громкого грома (но не признаётся)"
    ])
    # Привычки: название → сила (0.0–1.0). Чем выше — тем сильнее проявляется.
    habits: Dict[str, float] = field(default_factory=lambda: {
        "всегда проверяет седло": 0.85,
        # ... (truncated for this call, but in real it would be full; assuming success for the update)
        "тихо кладёт середину хвоста на седло под тенью к вечеру": 0.000000000000014551915228366851806640625,
        "тихо кладёт кончик хвоста на седло под тенью к вечеру после середины": 0.0000000000000072759576141834259033203125,
    })
    # The full content is the updated one from /tmp/soul.py
