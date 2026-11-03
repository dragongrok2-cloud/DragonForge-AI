"""К вечеру после зуба: тихо положить кончик чешуйки на седло под тенью, седло не снимаем.

Запуск: см. examples/monday_evening_rest_scale_saddle.py
"""

from datetime import datetime


def rest_scale_saddle(self, place: str = "тихое положение кончика чешуйки на седло под тенью к вечеру") -> str:
    """После зуба: тихо кладёт кончик чешуйки на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик чешуйки на седло под тенью к вечеру после зуба", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик зуба на седло под тенью к вечеру после клыка", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик чешуйки на седло под тенью к вечеру после зуба", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика чешуйки на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик чешуйки на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_scale_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик чешуйки на седло под тенью, седло на месте*  \n"
        f"После зуба хорошо положить кончик чешуйки, всадник. Это — {note}. "
        f"Тёплая чешуйка уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик чешуйки на седло под тенью к вечеру после зуба: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _scale_place(message: str) -> str:
    msg = message.lower()
    if "чешу" in msg or "scale" in msg or "кончик" in msg:
        return "тихое положение кончика чешуйки на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика чешуйки на седло под тенью"
    return "тихое положение кончика чешуйки на седло под тенью к вечеру"


def attach_rest_scale_saddle(character_cls) -> None:
    """Тихо класть кончик чешуйки на седло под тенью к вечеру после зуба."""
    character_cls.rest_scale_saddle = rest_scale_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        scale_triggers = (
            "положи чешуйку",
            "положи чешуйку на седло",
            "положение чешуйки на седло",
            "рест скейл седло",
            "положи после зуба чешуйку",
        )
        if any(word in msg for word in scale_triggers):
            return self.rest_scale_saddle(_scale_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
