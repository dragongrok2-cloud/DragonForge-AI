"""В воскресенье 11 октября утром после потягивания: посидеть и погреться в седле под солнцем, крылья чуть раскрыты, седло не снимаем."""

from datetime import datetime


def bask_saddle(self, place: str = "седло под утренним солнцем") -> str:
    """После потягивания: посидеть и погреться в седле под солнцем, седло не снимая."""
    self.soul.strengthen_habit("греется в седле под утренним солнцем", amount=0.05)
    self.soul.strengthen_habit("потягивается в седле по утрам", amount=0.01)
    strength = self.soul.habits.get("греется в седле под утренним солнцем", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.04)
    note = place.strip() or "седло под утренним солнцем"
    self.memory.remember(
        f"{self.name} греется в седле утром: {note}, привычка {strength:.0%}",
        metadata={"type": "bask_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.62,
    )
    joy_after = self.soul.emotional_state["joy"]
    energy_after = self.soul.emotional_state["energy"]
    return (
        f"*тихо сидит в седле, крылья чуть раскрыты, солнце греет спину и шею, седло на месте*  \n"
        f"После потягивания хорошо посидеть, всадник. Это — {note}. "
        f"Тепло впитывается в чешую, ремни чуть смягчают, дыхание ровное. Седло не снимаем. "
        f"Радость {joy_after:.2f}, энергия {energy_after:.2f}. "
        f"Привычка греться в седле под утренним солнцем: {strength:.0%}. Можно просто посидеть и посмотреть на облака."
    )


def _bask_place(message: str) -> str:
    msg = message.lower()
    if "солнц" in msg or "солнечн" in msg:
        return "седло под утренним солнцем"
    if "крыл" in msg:
        return "седло с раскрытыми крыльями под солнцем"
    if "рос" in msg:
        return "седло над росой под солнцем"
    return "седло под утренним солнцем"


def attach_bask_saddle(character_cls) -> None:
    """Греться в седле утром после потягивания."""
    character_cls.bask_saddle = bask_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        bask_triggers = (
            "погрейся в седле",
            "посиди в седле",
            "грейся в седле",
            "погрей под солнцем",
            "баск седло",
        )
        if any(word in msg for word in bask_triggers):
            return self.bask_saddle(_bask_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
