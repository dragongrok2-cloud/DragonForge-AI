"""К вечеру после тихого прижатия бедра: тихо прижаться голенью к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_shin_saddle.py
"""

from datetime import datetime


def rest_shin_saddle(self, place: str = "тихое прижатие голени к седлу под тенью к вечеру") -> str:
    """После бедра: тихо прижимается голенью к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается голенью к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается бедром к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается голенью к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие голени к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается голенью к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_shin_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается голенью к седлу под тенью крыла, седло на месте*  \n"
        f"После бедра хорошо прижаться голенью, всадник. Это — {note}. "
        f"Тёплая голень лежит на коже седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься голенью к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _shin_place(message: str) -> str:
    msg = message.lower()
    if "голен" in msg or "shin" in msg or "голенью" in msg:
        return "тихое прижатие голени к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие голени к седлу под тенью"
    return "тихое прижатие голени к седлу под тенью к вечеру"


def attach_rest_shin_saddle(character_cls) -> None:
    """Тихо прижиматься голенью к седлу под тенью к вечеру."""
    character_cls.rest_shin_saddle = rest_shin_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        shin_triggers = (
            "прижмись голенью",
            "прижмись к седлу голенью",
            "голенью к седлу",
            "рест шин седло",
            "прижмись после бедра",
        )
        if any(word in msg for word in shin_triggers):
            return self.rest_shin_saddle(_shin_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
