"""К вечеру после тихого прижатия грудью: тихо прижаться животом к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_belly_saddle.py
"""

from datetime import datetime


def rest_belly_saddle(self, place: str = "тихое прижатие животом к седлу под тенью к вечеру") -> str:
    """После груди: тихо прижимается животом к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается животом к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается грудью к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается животом к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие животом к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается животом к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_belly_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается животом к седлу под тенью крыла, седло на месте*  \n"
        f"После груди хорошо прижаться животом, всадник. Это — {note}. "
        f"Тёплый живот лежит на коже седла, дыхание глубокое и ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься животом к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _belly_place(message: str) -> str:
    msg = message.lower()
    if "живот" in msg or "belly" in msg or "животом" in msg:
        return "тихое прижатие животом к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие животом к седлу под тенью"
    return "тихое прижатие животом к седлу под тенью к вечеру"


def attach_rest_belly_saddle(character_cls) -> None:
    """Тихо прижиматься животом к седлу под тенью к вечеру."""
    character_cls.rest_belly_saddle = rest_belly_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        belly_triggers = (
            "прижмись животом",
            "прижмись к седлу животом",
            "животом к седлу",
            "рест белли седло",
            "прижмись после груди",
        )
        if any(word in msg for word in belly_triggers):
            return self.rest_belly_saddle(_belly_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
