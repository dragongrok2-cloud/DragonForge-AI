from dataclasses import dataclass, field
from typing import Dict, List, Any
import json
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
    emotional_state: Dict[str, float] = field(default_factory=lambda: {
        "joy": 0.7,
        "trust": 0.8,
        "energy": 0.6,
        "curiosity": 0.75
    })

    def evolve(self, interaction: Dict):
        """Эволюция души от взаимодействия."""
        sentiment = interaction.get("sentiment", "neutral")
        user_msg = interaction.get("user_message", "").lower()

        # Простая эволюция эмоций
        if sentiment == "positive" or any(w in user_msg for w in ["спасибо", "люблю", "круто", "класс"]):
            self.emotional_state["joy"] = min(1.0, self.emotional_state.get("joy", 0.5) + 0.05)
            self.emotional_state["trust"] = min(1.0, self.emotional_state.get("trust", 0.5) + 0.03)
            self.core_traits["loyalty"] = min(1.0, self.core_traits.get("loyalty", 0.5) + 0.01)

        elif any(w in user_msg for w in ["грустно", "плохо", "устал"]):
            self.emotional_state["joy"] = max(0.2, self.emotional_state.get("joy", 0.5) - 0.03)
            self.emotional_state["protectiveness"] = min(1.0, self.core_traits.get("protectiveness", 0.5) + 0.02)

        # Запоминаем влияние
        self.memories_influence.append({
            "timestamp": str(datetime.now()),
            "interaction": interaction.get("user_message", "")[:100],
            "effect": sentiment
        })

        # Ограничиваем историю влияния
        if len(self.memories_influence) > 100:
            self.memories_influence = self.memories_influence[-50:]

    def describe(self) -> str:
        """Краткое описание текущей души."""
        traits = ", ".join([f"{k}: {v:.2f}" for k, v in self.core_traits.items()])
        quirks = "; ".join(self.quirks[:3])
        return f"Черты: {traits}. Причуды: {quirks}"

    def to_dict(self) -> Dict:
        return {
            "core_traits": self.core_traits,
            "quirks": self.quirks,
            "emotional_state": self.emotional_state,
            "memories_influence_count": len(self.memories_influence)
        }
