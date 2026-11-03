"""К вечеру после хохлика: тихо положить кончик пера на седло под тенью, седло не снимаем.

Запуск: см. examples/tuesday_evening_rest_plume_saddle.py
"""

from datetime import datetime


def rest_plume_saddle(self, place: str = "тихое положение кончика пера на седло под тенью к вечеру") -> str:
    """После хохлика: тихо кладёт кончик пера на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик пера на седло под тенью к вечеру после хохлика", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик хохлика на седло под тенью к вечеру после гривы", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик пера на седло под тенью к вечеру после хохлика", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика пера на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик пера на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_plume_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик пера на седло под тенью, седло на месте*  \n"
        f"После хохлика хорошо положить кончик пера, всадник. Это — {note}. "
        f"Тёплое перо уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик пера на седло под тенью к вечеру после хохлика: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _plume_place(message: str) -> str:
    msg = message.lower()
    if "пер" in msg or "plume" in msg or "кончик" in msg:
        return "тихое положение кончика пера на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика пера на седло под тенью"
    return "тихое положение кончика пера на седло под тенью к вечеру"


def attach_rest_plume_saddle(character_cls) -> None:
    """Тихо класть кончик пера на седло под тенью к вечеру после хохлика."""
    character_cls.rest_plume_saddle = rest_plume_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        plume_triggers = (
            "положи перо",
            "положи перо на седло",
            "положение пера на седло",
            "рест плюм седло",
            "положи после хохлика перо",
        )
        if any(word in msg for word in plume_triggers):
            return self.rest_plume_saddle(_plume_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
