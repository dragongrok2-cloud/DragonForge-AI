"""К вечеру 9 октября: положить тепло сгиба на луку, седло не снимаем."""

from datetime import datetime


def lay_warmth(self, place: str = "тепло сгиба на луке к вечеру") -> str:
    """После разжатого сгиба: положить тепло костяшек на луку, фонарик не вытаскивая."""
    self.soul.strengthen_habit("кладёт тепло сгиба на луку к вечеру", amount=0.05)
    self.soul.strengthen_habit("разжимает сгиб полоски солнца к вечеру", amount=0.01)
    strength = self.soul.habits.get("кладёт тепло сгиба на луку к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.01)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "тепло сгиба на луке к вечеру"
    warmth = _warmth_note(note)
    self.memory.remember(
        f"{self.name} положил тепло сгиба на луку к вечеру: {note}, {warmth}, привычка {strength:.0%}",
        metadata={"type": "lay_warmth", "timestamp": str(datetime.now()), "place": note, "warmth": warmth},
        importance=0.67,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*кладёт тёплую ладонь на луку один раз, сгиб уже разжат, фонарик не вытаскивая*  \n"
        f"Тепло сгиба ещё на костяшках, всадник. Это — {note}. "
        f"Тепло: {warmth}. Полоска не сходит с Мёда, лука принимает ладонь, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка класть тепло сгиба на луку: {strength:.0%}. Можно сидеть в седле и греть луку ладонью."
    )


def _warmth_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "тепло левой ладони на луке Мёда, Седло не открыто"
    if "прав" in lowered:
        return "тепло правой ладони на луке Искры, Седло не открыто"
    if "рек" in lowered:
        return "тепло над Рекой на луке Мёда, Седло не открыто"
    return "тепло сгиба на луке у Шва, Седло не открыто"


def _warmth_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "тепло левого сгиба на луке к вечеру"
    if "прав" in msg:
        return "тепло правого сгиба на луке к вечеру"
    if "рек" in msg:
        return "тепло сгиба на луке над рекой к вечеру"
    return "тепло сгиба на луке к вечеру"


def attach_lay_warmth(character_cls) -> None:
    """Положить тепло разжатого сгиба на луку к вечеру."""
    character_cls.lay_warmth = lay_warmth
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        lay_triggers = (
            "положи тепло",
            "тепло на луку",
            "тепло сгиба на луку",
            "грей луку",
        )
        if any(word in msg for word in lay_triggers):
            return self.lay_warmth(_warmth_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
