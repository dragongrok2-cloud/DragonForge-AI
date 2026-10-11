"""В воскресенье 11 октября в полдень после тени крыла: делает глоток в седле, термос или облачная ягода, седло не снимаем.

Запуск: см. examples/sunday_midday_sip_saddle.py
"""

from datetime import datetime


def sip_saddle(self, place: str = "глоток в седле под тенью в полдень") -> str:
    """После тени крыла: делает глоток в седле, седло не снимая."""
    self.soul.strengthen_habit("делает глоток в седле под тенью в полдень", amount=0.05)
    self.soul.strengthen_habit("даёт тень крылом в седле в полдень", amount=0.01)
    strength = self.soul.habits.get("делает глоток в седле под тенью в полдень", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "глоток в седле под тенью в полдень"
    self.memory.remember(
        f"{self.name} делает глоток в седле под тенью в полдень: {note}, привычка {strength:.0%}",
        metadata={"type": "sip_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.61,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо сидит в седле под тенью крыла, делает глоток из термоса, седло на месте*  \n"
        f"После тени хорошо глотнуть, всадник. Это — {note}. "
        f"Прохлада крыла, термос тёплый или ягодный сок, дыхание ровное. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка делать глоток в седле под тенью в полдень: {strength:.0%}. Можно посидеть в прохладе и посмотреть на горизонт."
    )


def _sip_place(message: str) -> str:
    msg = message.lower()
    if "термос" in msg:
        return "глоток из термоса в седле под тенью"
    if "ягод" in msg or "облачн" in msg:
        return "глоток облачной ягоды в седле под тенью"
    if "горизонт" in msg:
        return "глоток в седле с видом на горизонт"
    return "глоток в седле под тенью в полдень"


def attach_sip_saddle(character_cls) -> None:
    """Делать глоток в седле под тенью в полдень."""
    character_cls.sip_saddle = sip_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        sip_triggers = (
            "сделай глоток в седле",
            "глоток в седле",
            "поделись глотком",
            "сип седло",
            "глоток после тени",
        )
        if any(word in msg for word in sip_triggers):
            return self.sip_saddle(_sip_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
