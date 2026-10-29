"""В воскресенье 11 октября к вечеру после тихого прижатия носом: тихо прижаться ухом к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_ear_saddle.py
"""

from datetime import datetime


def rest_ear_saddle(self, place: str = "тихое прижатие уха к седлу под тенью к вечеру") -> str:
    """После носа: тихо прижимается ухом к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается ухом к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается носом к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается ухом к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие уха к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается ухом к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_ear_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается ухом к седлу под тенью крыла, седло на месте*  \n"
        f"После носа хорошо прижаться ухом, всадник. Это — {note}. "
        f"Тёплое ухо касается кожи седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься ухом к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _ear_place(message: str) -> str:
    msg = message.lower()
    if "ухом" in msg or "ear" in msg or "ушк" in msg:
        return "тихое прижатие уха к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие уха к седлу под тенью"
    return "тихое прижатие уха к седлу под тенью к вечеру"


def attach_rest_ear_saddle(character_cls) -> None:
    """Тихо прижиматься ухом к седлу под тенью к вечеру."""
    character_cls.rest_ear_saddle = rest_ear_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        ear_triggers = (
            "прижмись ухом",
            "прижмись к седлу ухом",
            "ухом к седлу",
            "рест ир седло",
            "прижмись после носа",
        )
        if any(word in msg for word in ear_triggers):
            return self.rest_ear_saddle(_ear_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
