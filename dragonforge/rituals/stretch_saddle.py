"""В воскресенье 11 октября утром: мягко потягивается в седле под утренним солнцем, крылья раскрывает чуть шире, седло не снимаем."""

from datetime import datetime


def stretch_saddle(self, place: str = "седло под утренним солнцем") -> str:
    """Утром: мягко потягивается в седле под солнцем, седло не снимая."""
    self.soul.strengthen_habit("потягивается в седле по утрам", amount=0.05)
    self.soul.strengthen_habit("дремлет в седле к ночи", amount=0.01)
    strength = self.soul.habits.get("потягивается в седле по утрам", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.06)
    note = place.strip() or "седло под утренним солнцем"
    self.memory.remember(
        f"{self.name} мягко потягивается в седле утром: {note}, привычка {strength:.0%}",
        metadata={"type": "stretch_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.65,
    )
    joy_after = self.soul.emotional_state["joy"]
    energy_after = self.soul.emotional_state["energy"]
    return (
        f"*мягко потягивается в седле, крылья раскрываются чуть шире, солнце греет спину, седло на месте*  \n"
        f"Утро тихо пришло, всадник. Это — {note}. "
        f"Тело потянулось, ремни чуть скрипят, дыхание стало глубже. Седло не снимаем. "
        f"Радость {joy_after:.2f}, энергия {energy_after:.2f}. "
        f"Привычка потягиваться в седле по утрам: {strength:.0%}. Можно посидеть и встретить солнце."
    )


def _stretch_place(message: str) -> str:
    msg = message.lower()
    if "солнц" in msg or "солнечн" in msg:
        return "седло под утренним солнцем"
    if "крыл" in msg:
        return "седло с раскрытыми крыльями утром"
    if "рос" in msg:
        return "седло над росой утром"
    return "седло под утренним солнцем"


def attach_stretch_saddle(character_cls) -> None:
    """Потягиваться в седле утром."""
    character_cls.stretch_saddle = stretch_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        stretch_triggers = (
            "потянись в седле",
            "растянись в седле",
            "потягивание в седле",
            "утреннее потягивание",
            "стретч седло",
        )
        if any(word in msg for word in stretch_triggers):
            return self.stretch_saddle(_stretch_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
