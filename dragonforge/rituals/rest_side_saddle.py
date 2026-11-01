"""К вечеру после тихого прижатия спиной: тихо прижаться боком к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_side_saddle.py
"""

from datetime import datetime


def rest_side_saddle(self, place: str = "тихое прижатие боком к седлу под тенью к вечеру") -> str:
    """После спины: тихо прижимается боком к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается боком к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается спиной к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается боком к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие боком к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается боком к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_side_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается боком к седлу под тенью крыла, седло на месте*  \n"
        f"После спины хорошо прижаться боком, всадник. Это — {note}. "
        f"Тёплый бок лежит на коже седла, дыхание глубокое и ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься боком к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _side_place(message: str) -> str:
    msg = message.lower()
    if "бок" in msg or "side" in msg or "боком" in msg:
        return "тихое прижатие боком к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие боком к седлу под тенью"
    return "тихое прижатие боком к седлу под тенью к вечеру"


def attach_rest_side_saddle(character_cls) -> None:
    """Тихо прижиматься боком к седлу под тенью к вечеру."""
    character_cls.rest_side_saddle = rest_side_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        side_triggers = (
            "прижмись боком",
            "прижмись к седлу боком",
            "боком к седлу",
            "рест сайд седло",
            "прижмись после спины",
        )
        if any(word in msg for word in side_triggers):
            return self.rest_side_saddle(_side_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
