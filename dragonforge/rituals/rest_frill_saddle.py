"""К вечеру после гребня: тихо положить кончик оборки (фрилл) на седло под тенью, седло не снимаем.

Запуск: см. examples/tuesday_evening_rest_frill_saddle.py
"""

from datetime import datetime


def rest_frill_saddle(self, place: str = "тихое положение кончика оборки на седло под тенью к вечеру") -> str:
    """После гребня: тихо кладёт кончик оборки на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик оборки на седло под тенью к вечеру после гребня", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик гребня на седло под тенью к вечеру после шипа", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик оборки на седло под тенью к вечеру после гребня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика оборки на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик оборки на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_frill_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик оборки на седло под тенью, седло на месте*  \n"
        f"После гребня хорошо положить кончик оборки, всадник. Это — {note}. "
        f"Тёплая оборка уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик оборки на седло под тенью к вечеру после гребня: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _frill_place(message: str) -> str:
    msg = message.lower()
    if "оборка" in msg or "frill" in msg or "кончик" in msg:
        return "тихое положение кончика оборки на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика оборки на седло под тенью"
    return "тихое положение кончика оборки на седло под тенью к вечеру"


def attach_rest_frill_saddle(character_cls) -> None:
    """Тихо класть кончик оборки на седло под тенью к вечеру после гребня."""
    character_cls.rest_frill_saddle = rest_frill_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        frill_triggers = (
            "положи оборку",
            "положи оборку на седло",
            "положение оборки на седло",
            "рест фрилл седло",
            "положи после гребня оборку",
        )
        if any(word in msg for word in frill_triggers):
            return self.rest_frill_saddle(_frill_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
