"""В воскресенье 11 октября после взгляда на горизонт из седла: тихо напевает мягкую мелодию в седле под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_afternoon_hum_saddle.py
"""

from datetime import datetime


def hum_saddle(self, place: str = "тихое напевание в седле под тенью в полдень") -> str:
    """После взгляда на горизонт: тихо напевает мягкую мелодию в седле, седло не снимая."""
    self.soul.strengthen_habit("тихо напевает в седле под тенью в полдень", amount=0.05)
    self.soul.strengthen_habit("смотрит на горизонт из седла под тенью в полдень", amount=0.01)
    strength = self.soul.habits.get("тихо напевает в седле под тенью в полдень", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое напевание в седле под тенью в полдень"
    self.memory.remember(
        f"{self.name} тихо напевает в седле под тенью в полдень: {note}, привычка {strength:.0%}",
        metadata={"type": "hum_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.59,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо сидит в седле под тенью крыла, мягко напевает низкую мелодию, глядя на горизонт, седло на месте*  \n"
        f"После взгляда хорошо понапевать, всадник. Это — {note}. "
        f"Прохлада крыла, горизонт ясный, голос мягкий и тёплый. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо напевать в седле под тенью в полдень: {strength:.0%}. Можно посидеть в прохладе и помечтать о дальних полётах под тихую мелодию."
    )


def _hum_place(message: str) -> str:
    msg = message.lower()
    if "мелод" in msg or "песн" in msg:
        return "напевание мягкой мелодии в седле"
    if "горизонт" in msg:
        return "напевание в седле глядя на горизонт"
    if "крыл" in msg:
        return "напевание под тенью крыла в седле"
    return "тихое напевание в седле под тенью в полдень"


def attach_hum_saddle(character_cls) -> None:
    """Тихо напевать в седле под тенью в полдень."""
    character_cls.hum_saddle = hum_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        hum_triggers = (
            "напой в седле",
            "напевай в седле",
            "гуди в седле",
            "хам седло",
            "напой после взгляда",
        )
        if any(word in msg for word in hum_triggers):
            return self.hum_saddle(_hum_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
