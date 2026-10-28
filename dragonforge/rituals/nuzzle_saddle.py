"""В воскресенье 11 октября к вечеру после тихого дремания в седле: тихо прижимается мордой к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_nuzzle_saddle.py
"""

from datetime import datetime


def nuzzle_saddle(self, place: str = "тихое прижатие морды к седлу под тенью к вечеру") -> str:
    """После дремания: тихо прижимается мордой к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается мордой к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо дремлет в седле под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается мордой к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.04)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие морды к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается мордой к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "nuzzle_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.60,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается мордой к седлу под тенью крыла, седло на месте*  \n"
        f"После дремания хорошо прижаться мордой, всадник. Это — {note}. "
        f"Мягкая чешуя касается кожи седла, тёплый выдох греет луку, глаза ещё полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься мордой к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _nuzzle_place(message: str) -> str:
    msg = message.lower()
    if "приж" in msg or "морд" in msg or "нузз" in msg:
        return "тихое прижатие морды к седлу"
    if "седл" in msg:
        return "прижатие к седлу под тенью"
    return "тихое прижатие морды к седлу под тенью к вечеру"


def attach_nuzzle_saddle(character_cls) -> None:
    """Тихо прижиматься мордой к седлу под тенью к вечеру."""
    character_cls.nuzzle_saddle = nuzzle_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        nuzzle_triggers = (
            "прижмись к седлу",
            "прижмись мордой",
            "нуззл седло",
            "тихо прижмись",
            "прижмись после дремания",
        )
        if any(word in msg for word in nuzzle_triggers):
            return self.nuzzle_saddle(_nuzzle_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
