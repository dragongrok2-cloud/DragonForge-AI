"""К позднему дню 8 октября: дыхание на уже затенённые петли."""

from datetime import datetime


def warm_loops(self, place: str = "дыхание на петлях медового узелка к позднему дню") -> str:
    """После тени: согреть названные петли дыханием, не развязывая узелок и не снимая седла."""
    self.soul.strengthen_habit("согревает петли медового узелка дыханием к позднему дню", amount=0.05)
    self.soul.strengthen_habit("накрывает петли медового узелка тенью после полудня", amount=0.01)
    strength = self.soul.habits.get("согревает петли медового узелка дыханием к позднему дню", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "дыхание на петлях медового узелка к позднему дню"
    warmth = _warmth_note(note)
    self.memory.remember(
        f"{self.name} согрел петли медового узелка дыханием к позднему дню: {note}, {warmth}, привычка {strength:.0%}",
        metadata={"type": "warm_loops", "timestamp": str(datetime.now()), "place": note, "warmth": warmth},
        importance=0.62,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*к позднему дню тихо дышит на затенённые петли, не развязывая узелок, седло на месте*  \n"
        f"Тень уже легла, всадник. Это — {note}. "
        f"Тепло короткое: {warmth}. Нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка согревать петли медового узелка дыханием: {strength:.0%}. Можно сидеть в седле, пока день стынет."
    )


def _warmth_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "тепло на Мёде, Шов ещё в тени, Седло не стынет"
    if "прав" in lowered:
        return "тепло на Искре, Шов ещё в тени, Седло не стынет"
    if "рек" in lowered:
        return "тепло на Реке, Мёд ещё в тени, Седло не стынет"
    return "тепло на Мёде, Шов ещё в тени, Седло не стынет"


def _warm_loops_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "дыхание на левых петлях медового узелка к позднему дню"
    if "прав" in msg:
        return "дыхание на правых петлях медового узелка к позднему дню"
    if "рек" in msg:
        return "дыхание на петлях медового узелка над рекой к позднему дню"
    return "дыхание на петлях медового узелка к позднему дню"


def attach_warm(character_cls) -> None:
    """Повесить дыхание поверх тени петель."""
    character_cls.warm_loops = warm_loops
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        warm_triggers = (
            "согрей петл",
            "погрей петл",
            "дыхание на петл",
            "подыши на петл",
            "тепл петл",
        )
        if any(word in msg for word in warm_triggers):
            return self.warm_loops(_warm_loops_note(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
