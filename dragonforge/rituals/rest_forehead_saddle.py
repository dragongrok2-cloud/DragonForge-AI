"""В воскресенье 11 октября к вечеру после тихого прижатия щекой: тихо прижаться лбом к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_forehead_saddle.py
"""

from datetime import datetime


def rest_forehead_saddle(self, place: str = "тихое прижатие лба к седлу под тенью к вечеру") -> str:
    """После щеки: тихо прижимается лбом к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается лбом к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается щекой к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается лбом к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие лба к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается лбом к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_forehead_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается лбом к седлу под тенью крыла, седло на месте*  \n"
        f"После щеки хорошо прижаться лбом, всадник. Это — {note}. "
        f"Тёплый лоб касается кожи седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься лбом к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _forehead_place(message: str) -> str:
    msg = message.lower()
    if "лбом" in msg or "forehead" in msg:
        return "тихое прижатие лба к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие лба к седлу под тенью"
    return "тихое прижатие лба к седлу под тенью к вечеру"


def attach_rest_forehead_saddle(character_cls) -> None:
    """Тихо прижиматься лбом к седлу под тенью к вечеру."""
    character_cls.rest_forehead_saddle = rest_forehead_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        forehead_triggers = (
            "прижмись лбом",
            "прижмись к седлу лбом",
            "лбом к седлу",
            "рест форхед седло",
            "прижмись после щеки",
        )
        if any(word in msg for word in forehead_triggers):
            return self.rest_forehead_saddle(_forehead_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
