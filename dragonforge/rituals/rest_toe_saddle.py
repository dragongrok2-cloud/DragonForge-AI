"""К вечеру после тихого прижатия лапы: тихо прижаться пальцем лапы к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_toe_saddle.py
"""

from datetime import datetime


def rest_toe_saddle(self, place: str = "тихое прижатие пальца лапы к седлу под тенью к вечеру") -> str:
    """После лапы: тихо прижимается пальцем лапы к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается пальцем лапы к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается лапой к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается пальцем лапы к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие пальца лапы к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается пальцем лапы к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_toe_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается пальцем лапы к седлу под тенью крыла, седло на месте*  \n"
        f"После лапы хорошо прижаться пальцем, всадник. Это — {note}. "
        f"Тёплый палец лапы лежит на коже седла, коготь чуть втянут, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься пальцем лапы к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _toe_place(message: str) -> str:
    msg = message.lower()
    if "пальц" in msg or "toe" in msg or "пальцем" in msg:
        return "тихое прижатие пальца лапы к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие пальца лапы к седлу под тенью"
    return "тихое прижатие пальца лапы к седлу под тенью к вечеру"


def attach_rest_toe_saddle(character_cls) -> None:
    """Тихо прижиматься пальцем лапы к седлу под тенью к вечеру."""
    character_cls.rest_toe_saddle = rest_toe_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        toe_triggers = (
            "прижмись пальцем",
            "прижмись к седлу пальцем",
            "пальцем к седлу",
            "рест то седло",
            "прижмись после лапы",
        )
        if any(word in msg for word in toe_triggers):
            return self.rest_toe_saddle(_toe_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
