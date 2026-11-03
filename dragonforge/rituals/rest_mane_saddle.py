"""К вечеру после усика: тихо положить кончик гривы на седло под тенью, седло не снимаем.

Запуск: см. examples/monday_evening_rest_mane_saddle.py
"""

from datetime import datetime


def rest_mane_saddle(self, place: str = "тихое положение кончика гривы на седло под тенью к вечеру") -> str:
    """После усика: тихо кладёт кончик гривы на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик гривы на седло под тенью к вечеру после усика", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик усика на седло под тенью к вечеру после чешуйки", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик гривы на седло под тенью к вечеру после усика", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика гривы на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик гривы на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_mane_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик гривы на седло под тенью, седло на месте*  \n"
        f"После усика хорошо положить кончик гривы, всадник. Это — {note}. "
        f"Тёплая грива уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик гривы на седло под тенью к вечеру после усика: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _mane_place(message: str) -> str:
    msg = message.lower()
    if "грив" in msg or "mane" in msg or "кончик" in msg:
        return "тихое положение кончика гривы на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика гривы на седло под тенью"
    return "тихое положение кончика гривы на седло под тенью к вечеру"


def attach_rest_mane_saddle(character_cls) -> None:
    """Тихо класть кончик гривы на седло под тенью к вечеру после усика."""
    character_cls.rest_mane_saddle = rest_mane_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        mane_triggers = (
            "положи гриву",
            "положи гриву на седло",
            "положение гривы на седло",
            "рест мэйн седло",
            "положи после усика гриву",
        )
        if any(word in msg for word in mane_triggers):
            return self.rest_mane_saddle(_mane_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
