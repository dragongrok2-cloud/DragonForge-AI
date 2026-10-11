"""В воскресенье 11 октября в полдень после глотка в седле: смотрит на горизонт из седла под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_afternoon_gaze_saddle.py
"""

from datetime import datetime


def gaze_saddle(self, place: str = "взгляд на горизонт из седла под тенью в полдень") -> str:
    """После глотка в седле: смотрит на горизонт под тенью крыла, седло не снимая."""
    self.soul.strengthen_habit("смотрит на горизонт из седла под тенью в полдень", amount=0.05)
    self.soul.strengthen_habit("делает глоток в седле под тенью в полдень", amount=0.01)
    strength = self.soul.habits.get("смотрит на горизонт из седла под тенью в полдень", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "взгляд на горизонт из седла под тенью в полдень"
    self.memory.remember(
        f"{self.name} смотрит на горизонт из седла под тенью в полдень: {note}, привычка {strength:.0%}",
        metadata={"type": "gaze_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.60,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо сидит в седле под тенью крыла, смотрит вдаль на горизонт, седло на месте*  \n"
        f"После глотка хорошо посмотреть вдаль, всадник. Это — {note}. "
        f"Прохлада крыла, горизонт ясный, дыхание ровное. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка смотреть на горизонт из седла под тенью в полдень: {strength:.0%}. Можно посидеть в прохладе и помечтать о дальних полётах."
    )


def _gaze_place(message: str) -> str:
    msg = message.lower()
    if "облак" in msg:
        return "взгляд на горизонт сквозь облака из седла"
    if "хребет" in msg or "гор" in msg:
        return "взгляд на хребет на горизонте из седла"
    if "даль" in msg:
        return "дальний взгляд на горизонт из седла"
    return "взгляд на горизонт из седла под тенью в полдень"


def attach_gaze_saddle(character_cls) -> None:
    """Смотреть на горизонт из седла под тенью в полдень."""
    character_cls.gaze_saddle = gaze_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        gaze_triggers = (
            "посмотри на горизонт",
            "взгляд в седле",
            "горизонт после глотка",
            "гейз седло",
            "посмотри вдаль",
        )
        if any(word in msg for word in gaze_triggers):
            return self.gaze_saddle(_gaze_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
