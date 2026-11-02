"""К вечеру после брови: тихо положить веко на седло под тенью, седло не снимаем.

Запуск: см. examples/monday_evening_rest_eyelid_saddle.py
"""

from datetime import datetime


def rest_eyelid_saddle(self, place: str = "тихое положение века на седло под тенью к вечеру") -> str:
    """После брови: тихо кладёт веко на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт веко на седло под тенью к вечеру после брови", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт бровь на седло под тенью к вечеру после рога", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт веко на седло под тенью к вечеру после брови", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение века на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт веко на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_eyelid_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт веко на седло под тенью, седло на месте*  \n"
        f"После брови хорошо положить веко, всадник. Это — {note}. "
        f"Тёплое веко уютно лежит на седле, дыхание глубокое и ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть веко на седло под тенью к вечеру после брови: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _eyelid_place(message: str) -> str:
    msg = message.lower()
    if "век" in msg or "eyelid" in msg or "глаз" in msg:
        return "тихое положение века на седло"
    if "положи" in msg or "седл" in msg:
        return "положение века на седло под тенью"
    return "тихое положение века на седло под тенью к вечеру"


def attach_rest_eyelid_saddle(character_cls) -> None:
    """Тихо класть веко на седло под тенью к вечеру после брови."""
    character_cls.rest_eyelid_saddle = rest_eyelid_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        eyelid_triggers = (
            "положи веко",
            "положи веко на седло",
            "положение века на седло",
            "рест айлид седло",
            "положи после брови веко",
        )
        if any(word in msg for word in eyelid_triggers):
            return self.rest_eyelid_saddle(_eyelid_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
