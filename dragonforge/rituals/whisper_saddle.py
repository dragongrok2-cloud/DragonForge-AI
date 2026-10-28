"""В воскресенье 11 октября к вечеру после тихого прижатия мордой к седлу: тихо шепчет седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_whisper_saddle.py
"""

from datetime import datetime


def whisper_saddle(self, place: str = "тихий шёпот седлу под тенью к вечеру") -> str:
    """После прижатия мордой: тихо шепчет седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо шепчет седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается мордой к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо шепчет седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.04)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихий шёпот седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо шепчет седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "whisper_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.60,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо шепчет седлу под тенью крыла, седло на месте*  \n"
        f"После прижатия мордой хорошо шепнуть седлу, всадник. Это — {note}. "
        f"Мягкий шёпот греет кожу седла, тёплый выдох касается луки, глаза ещё полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо шептать седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _whisper_place(message: str) -> str:
    msg = message.lower()
    if "шеп" in msg or "шёп" in msg or "виспер" in msg:
        return "тихий шёпот седлу"
    if "седл" in msg:
        return "шёпот седлу под тенью"
    return "тихий шёпот седлу под тенью к вечеру"


def attach_whisper_saddle(character_cls) -> None:
    """Тихо шептать седлу под тенью к вечеру."""
    character_cls.whisper_saddle = whisper_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        whisper_triggers = (
            "шепни седлу",
            "пошепчи седлу",
            "виспер седло",
            "тихо шепни",
            "шепни после прижатия",
        )
        if any(word in msg for word in whisper_triggers):
            return self.whisper_saddle(_whisper_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
