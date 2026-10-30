"""К вечеру после тихого прижатия колена: тихо прижаться лодыжкой к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_ankle_saddle.py
"""

from datetime import datetime


def rest_ankle_saddle(self, place: str = "тихое прижатие лодыжки к седлу под тенью к вечеру") -> str:
    """После колена: тихо прижимается лодыжкой к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается лодыжкой к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается коленом к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается лодыжкой к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие лодыжки к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается лодыжкой к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_ankle_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается лодыжкой к седлу под тенью крыла, седло на месте*  \n"
        f"После колена хорошо прижаться лодыжкой, всадник. Это — {note}. "
        f"Тёплая лодыжка лежит на коже седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься лодыжкой к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _ankle_place(message: str) -> str:
    msg = message.lower()
    if "лодыж" in msg or "ankle" in msg or "лодыжкой" in msg:
        return "тихое прижатие лодыжки к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие лодыжки к седлу под тенью"
    return "тихое прижатие лодыжки к седлу под тенью к вечеру"


def attach_rest_ankle_saddle(character_cls) -> None:
    """Тихо прижиматься лодыжкой к седлу под тенью к вечеру."""
    character_cls.rest_ankle_saddle = rest_ankle_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        ankle_triggers = (
            "прижмись лодыжкой",
            "прижмись к седлу лодыжкой",
            "лодыжкой к седлу",
            "рест анкл седло",
            "прижмись после колена",
        )
        if any(word in msg for word in ankle_triggers):
            return self.rest_ankle_saddle(_ankle_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
