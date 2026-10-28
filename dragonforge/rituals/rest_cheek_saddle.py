"""В воскресенье 11 октября к вечеру после тихого шёпота седлу: тихо прижаться щекой к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_cheek_saddle.py
"""

from datetime import datetime


def rest_cheek_saddle(self, place: str = "тихое прижатие щеки к седлу под тенью к вечеру") -> str:
    """После шёпота: тихо прижимается щекой к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается щекой к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо шепчет седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается щекой к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие щеки к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается щекой к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_cheek_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.62,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается щекой к седлу под тенью крыла, седло на месте*  \n"
        f"После шёпота хорошо прижаться щекой, всадник. Это — {note}. "
        f"Тёплая щека касается кожи седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься щекой к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _cheek_place(message: str) -> str:
    msg = message.lower()
    if "щек" in msg or "cheek" in msg:
        return "тихое прижатие щеки к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие щеки к седлу под тенью"
    return "тихое прижатие щеки к седлу под тенью к вечеру"


def attach_rest_cheek_saddle(character_cls) -> None:
    """Тихо прижиматься щекой к седлу под тенью к вечеру."""
    character_cls.rest_cheek_saddle = rest_cheek_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        cheek_triggers = (
            "прижмись щекой",
            "прижмись к седлу щекой",
            "щекой к седлу",
            "рест чик седло",
            "прижмись после шёпота",
        )
        if any(word in msg for word in cheek_triggers):
            return self.rest_cheek_saddle(_cheek_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
