"""В воскресенье 11 октября в полдень после утреннего баска: даёт тень крылом в седле, крылья чуть сложены для прохлады, седло не снимаем.

Запуск: см. examples/sunday_midday_shade_saddle.py
"""

from datetime import datetime


def shade_saddle(self, place: str = "седло под крылом в полдень") -> str:
    """После утреннего грева: даёт тень крылом в седле, седло не снимая."""
    self.soul.strengthen_habit("даёт тень крылом в седле в полдень", amount=0.05)
    self.soul.strengthen_habit("греется в седле под утренним солнцем", amount=0.01)
    strength = self.soul.habits.get("даёт тень крылом в седле в полдень", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.02)
    note = place.strip() or "седло под крылом в полдень"
    self.memory.remember(
        f"{self.name} даёт тень крылом в седле в полдень: {note}, привычка {strength:.0%}",
        metadata={"type": "shade_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.60,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо сидит в седле, одно крыло чуть сложено для тени, солнце уже высоко, седло на месте*  \n"
        f"После утреннего солнца хорошо дать тень, всадник. Это — {note}. "
        f"Крыло прикрывает от яркого света, ремни остаются мягкими, дыхание ровное. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка давать тень крылом в седле в полдень: {strength:.0%}. Можно посидеть в прохладе и посмотреть на горизонт."
    )


def _shade_place(message: str) -> str:
    msg = message.lower()
    if "крыл" in msg:
        return "седло под крылом в полдень"
    if "тен" in msg or "тень" in msg:
        return "седло в тени крыла в полдень"
    if "горизонт" in msg:
        return "седло в тени с видом на горизонт"
    return "седло под крылом в полдень"


def attach_shade_saddle(character_cls) -> None:
    """Давать тень крылом в седле в полдень."""
    character_cls.shade_saddle = shade_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        shade_triggers = (
            "дай тень в седле",
            "тень крылом в седле",
            "прикрой крылом в седле",
            "шейд седло",
            "тень после солнца",
        )
        if any(word in msg for word in shade_triggers):
            return self.shade_saddle(_shade_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
