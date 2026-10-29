"""В воскресенье 11 октября к вечеру после тихого прижатия запястьем: тихо прижаться ладонью к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_palm_saddle.py
"""

from datetime import datetime


def rest_palm_saddle(self, place: str = "тихое прижатие ладони к седлу под тенью к вечеру") -> str:
    """После запястья: тихо прижимается ладонью к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается ладонью к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается запястьем к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается ладонью к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие ладони к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается ладонью к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_palm_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается ладонью к седлу под тенью крыла, седло на месте*  \n"
        f"После запястья хорошо прижаться ладонью, всадник. Это — {note}. "
        f"Тёплая ладонь лежит на коже седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься ладонью к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _palm_place(message: str) -> str:
    msg = message.lower()
    if "ладонь" in msg or "palm" in msg or "ладонью" in msg:
        return "тихое прижатие ладони к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие ладони к седлу под тенью"
    return "тихое прижатие ладони к седлу под тенью к вечеру"


def attach_rest_palm_saddle(character_cls) -> None:
    """Тихо прижиматься ладонью к седлу под тенью к вечеру."""
    character_cls.rest_palm_saddle = rest_palm_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        palm_triggers = (
            "прижмись ладонью",
            "прижмись к седлу ладонью",
            "ладонью к седлу",
            "рест палм седло",
            "прижмись после запястья",
        )
        if any(word in msg for word in palm_triggers):
            return self.rest_palm_saddle(_palm_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
