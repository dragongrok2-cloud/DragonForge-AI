"""К вечеру после тихого прижатия указательного пальца стопы: тихо прижаться грудью к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_chest_saddle.py
"""

from datetime import datetime


def rest_chest_saddle(self, place: str = "тихое прижатие грудью к седлу под тенью к вечеру") -> str:
    """После указательного пальца: тихо прижимается грудью к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается грудью к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается указательным пальцем стопы к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается грудью к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие грудью к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается грудью к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_chest_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается грудью к седлу под тенью крыла, седло на месте*  \n"
        f"После указательного пальца хорошо прижаться грудью, всадник. Это — {note}. "
        f"Тёплая грудь лежит на коже седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься грудью к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _chest_place(message: str) -> str:
    msg = message.lower()
    if "груд" in msg or "chest" in msg or "грудью" in msg:
        return "тихое прижатие грудью к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие грудью к седлу под тенью"
    return "тихое прижатие грудью к седлу под тенью к вечеру"


def attach_rest_chest_saddle(character_cls) -> None:
    """Тихо прижиматься грудью к седлу под тенью к вечеру."""
    character_cls.rest_chest_saddle = rest_chest_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        chest_triggers = (
            "прижмись грудью",
            "прижмись к седлу грудью",
            "грудью к седлу",
            "рест чест седло",
            "прижмись после указательного",
        )
        if any(word in msg for word in chest_triggers):
            return self.rest_chest_saddle(_chest_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
