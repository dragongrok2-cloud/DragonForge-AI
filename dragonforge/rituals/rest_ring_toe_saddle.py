"""К вечеру после тихого прижатия среднего пальца стопы: тихо прижаться безымянным пальцем стопы к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_ring_toe_saddle.py
"""

from datetime import datetime


def rest_ring_toe_saddle(self, place: str = "тихое прижатие безымянного пальца стопы к седлу под тенью к вечеру") -> str:
    """После среднего: тихо прижимается безымянным пальцем стопы к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается безымянным пальцем стопы к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается средним пальцем стопы к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается безымянным пальцем стопы к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие безымянного пальца стопы к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается безымянным пальцем стопы к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_ring_toe_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается безымянным пальцем стопы к седлу под тенью крыла, седло на месте*  \n"
        f"После среднего хорошо прижаться безымянным пальцем стопы, всадник. Это — {note}. "
        f"Тёплый безымянный палец лежит на коже седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься безымянным пальцем стопы к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _ring_toe_place(message: str) -> str:
    msg = message.lower()
    if "безымян" in msg or "ring" in msg or "безымянным" in msg:
        return "тихое прижатие безымянного пальца стопы к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие безымянного пальца стопы к седлу под тенью"
    return "тихое прижатие безымянного пальца стопы к седлу под тенью к вечеру"


def attach_rest_ring_toe_saddle(character_cls) -> None:
    """Тихо прижиматься безымянным пальцем стопы к седлу под тенью к вечеру."""
    character_cls.rest_ring_toe_saddle = rest_ring_toe_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        ring_toe_triggers = (
            "прижмись безымянным пальцем",
            "прижмись к седлу безымянным пальцем",
            "безымянным пальцем к седлу",
            "рест ринг то седло",
            "прижмись после среднего",
        )
        if any(word in msg for word in ring_toe_triggers):
            return self.rest_ring_toe_saddle(_ring_toe_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
