from dataclasses import dataclass, field
from typing import Dict, List, Any
import json

@dataclass
class Soul:
    core_traits: Dict[str, float]      # Например: {"loyalty": 0.95, "curiosity": 0.8}
    memories_influence: List[Dict]     # Как воспоминания меняют характер
    evolution_rules: Dict[str, Any]
    quirks: List[str]                  # "любит чесать за ухом", "боится грома" и т.д.
    emotional_state: Dict[str, float]  # current joy, anger, trust...

    def evolve(self, interaction: Dict):
        """Эволюция души от взаимодействия"""
        # Здесь будет логика изменения черт от опыта
        pass