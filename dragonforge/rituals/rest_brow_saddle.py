"""К вечеру после кончика рога: тихо положить бровь на седло под тенью, седло не снимаем.

Запуск: см. examples/monday_evening_rest_brow_saddle.py
"""

from datetime import datetime


def rest_brow_saddle(self, place: str = "тихое положение брови на седло под тенью к вечеру") -> str:
    """После кончика рога: тихо кладёт бровь на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт бровь на седло под тенью к вечеру после рога", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик рога на седло под тенью к вечеру после хвоста", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт бровь на седло под тенью к вечеру после рога", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение брови на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт бровь на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_brow_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт бровь на седло под тенью, седло на месте*  \n"
        f"После кончика рога хорошо положить бровь, всадник. Это — {note}. "
        f"Тёплая бровь уютно лежит на седле, дыхание глубокое и ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть бровь на седло под тенью к вечеру после рога: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _brow_place(message: str) -> str:
    msg = message.lower()
    if "бров" in msg or "brow" in msg or "лоб" in msg:
        return "тихое положение брови на седло"
    if "положи" in msg or "седл" in msg:
        return "положение брови на седло под тенью"
    return "тихое положение брови на седло под тенью к вечеру"


def attach_rest_brow_saddle(character_cls) -> None:
    """Тихо класть бровь на седло под тенью к вечеру после рога."""
    character_cls.rest_brow_saddle = rest_brow_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        brow_triggers = (
            "положи бровь",
            "положи бровь на седло",
            "положение брови на седло",
            "рест броу седло",
            "положи после рога бровь",
        )
        if any(word in msg for word in brow_triggers):
            return self.rest_brow_saddle(_brow_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
