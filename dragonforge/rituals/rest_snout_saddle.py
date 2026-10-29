"""В воскресенье 11 октября к вечеру после тихого прижатия лбом: тихо прижаться носом к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_snout_saddle.py
"""

from datetime import datetime


def rest_snout_saddle(self, place: str = "тихое прижатие носа к седлу под тенью к вечеру") -> str:
    """После лба: тихо прижимается носом к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается носом к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается лбом к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается носом к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие носа к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается носом к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_snout_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается носом к седлу под тенью крыла, седло на месте*  \n"
        f"После лба хорошо прижаться носом, всадник. Это — {note}. "
        f"Тёплый нос касается кожи седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься носом к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _snout_place(message: str) -> str:
    msg = message.lower()
    if "носом" in msg or "snout" in msg or "nose" in msg:
        return "тихое прижатие носа к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие носа к седлу под тенью"
    return "тихое прижатие носа к седлу под тенью к вечеру"


def attach_rest_snout_saddle(character_cls) -> None:
    """Тихо прижиматься носом к седлу под тенью к вечеру."""
    character_cls.rest_snout_saddle = rest_snout_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        snout_triggers = (
            "прижмись носом",
            "прижмись к седлу носом",
            "носом к седлу",
            "рест снаут седло",
            "прижмись после лба",
        )
        if any(word in msg for word in snout_triggers):
            return self.rest_snout_saddle(_snout_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
