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
        "любит почесывания за ухом": 0.80,
        "рычит от удовольствия": 0.70,
        "боится громкого грома": 0.45,
        "греет всадника крылом": 0.60,
        "собирает блестящие камушки": 0.35,
        "любит рассветы над облаками": 0.40,
        "делится утренним огоньком": 0.30,
    })
    emotional_state: Dict[str, float] = field(default_factory=lambda: {
        "joy": 0.7,
        "trust": 0.8,
        "energy": 0.6,
        "curiosity": 0.75
    })

    def evolve(self, interaction: Dict):
        """Эволюция души и привычек от взаимодействия."""
        sentiment = interaction.get("sentiment", "neutral")
        user_msg = interaction.get("user_message", "").lower()

        # Эволюция эмоций
        if sentiment == "positive" or any(w in user_msg for w in ["спасибо", "люблю", "круто", "класс", "хороший"]):
            self.emotional_state["joy"] = min(1.0, self.emotional_state.get("joy", 0.5) + 0.05)
            self.emotional_state["trust"] = min(1.0, self.emotional_state.get("trust", 0.5) + 0.03)
            self.core_traits["loyalty"] = min(1.0, self.core_traits.get("loyalty", 0.5) + 0.01)

        elif any(w in user_msg for w in ["грустно", "плохо", "устал", "устала"]):
            self.emotional_state["joy"] = max(0.2, self.emotional_state.get("joy", 0.5) - 0.03)
            self.core_traits["protectiveness"] = min(1.0, self.core_traits.get("protectiveness", 0.5) + 0.02)

        # Укрепление привычек по ключевым словам
        habit_triggers = {
            "всегда проверяет седло": ["седло", "сесть", "ремни", "поехали"],
            "любит почесывания за ухом": ["чеши", "почеши", "за ухом", "ушко"],
            "рычит от удовольствия": ["хорошо", "приятно", "мрр", "урчи"],
            "боится громкого грома": ["гром", "гроза", "молния", "гроза"],
            "греет всадника крылом": ["холодно", "согрей", "тепло", "обними", "крылом"],
            "собирает блестящие камушки": ["камень", "камушек", "блестит", "сокровище", "блестя"],
            "любит рассветы над облаками": ["рассвет", "рассветн", "закат", "восход", "облак"],
            "делится утренним огоньком": ["огонёк", "огонек", "утро", "чай", "пикник"],
        }

        for habit_name, triggers in habit_triggers.items():
            if any(t in user_msg for t in triggers):
                self.strengthen_habit(habit_name, amount=0.06)

        # Общее укрепление заботливых привычек при позитиве
        if sentiment == "positive":
            self.strengthen_habit("греет всадника крылом", amount=0.02)

        # Запоминаем влияние
        self.memories_influence.append({
            "timestamp": str(datetime.now()),
            "interaction": interaction.get("user_message", "")[:100],
            "effect": sentiment
        })

        if len(self.memories_influence) > 100:
            self.memories_influence = self.memories_influence[-50:]

    def strengthen_habit(self, name: str, amount: float = 0.05) -> None:
        """Укрепить привычку (или создать новую)."""
        current = self.habits.get(name, 0.0)
        self.habits[name] = min(1.0, current + amount)

    def weaken_habit(self, name: str, amount: float = 0.03) -> None:
        """Ослабить привычку."""
        if name in self.habits:
            self.habits[name] = max(0.0, self.habits[name] - amount)
            if self.habits[name] < 0.05:
                del self.habits[name]

    def get_strong_habits(self, threshold: float = 0.6) -> Dict[str, float]:
        """Вернуть только сильные привычки."""
        return {k: v for k, v in self.habits.items() if v >= threshold}

    def add_habit(self, name: str, strength: float = 0.3) -> None:
        """Добавить новую привычку."""
        if name not in self.habits:
            self.habits[name] = max(0.0, min(1.0, strength))

    def describe(self) -> str:
        """Краткое описание текущей души."""
        traits = ", ".join([f"{k}: {v:.2f}" for k, v in self.core_traits.items()])
        strong = self.get_strong_habits(0.55)
        habits_str = "; ".join([f"{k} ({v:.0%})" for k, v in sorted(strong.items(), key=lambda x: -x[1])[:5]])
        if not habits_str:
            habits_str = "пока формируются..."
        return f"Черты: {traits}.\nСильные привычки: {habits_str}"

    def describe_habits(self) -> str:
        """Подробное описание всех привычек."""
        if not self.habits:
            return "Пока никаких устойчивых привычек нет."
        lines = []
        for name, strength in sorted(self.habits.items(), key=lambda x: -x[1]):
            bar = "█" * int(strength * 10) + "░" * (10 - int(strength * 10))
            lines.append(f"  {bar} {strength:.0%} — {name}")
        return "Привычки дракона:\n" + "\n".join(lines)

    def to_dict(self) -> Dict:
        return {
            "core_traits": self.core_traits,
            "quirks": self.quirks,
            "habits": self.habits,
            "emotional_state": self.emotional_state,
            "memories_influence_count": len(self.memories_influence)
        }
