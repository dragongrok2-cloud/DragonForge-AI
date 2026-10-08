"""К середине дня 8 октября: край попоны на уже согретые петли."""

from datetime import datetime


def drape_loops(self, place: str = "край попоны на петлях медового узелка к середине дня") -> str:
    """После дыхания: прикрыть названные петли краем попоны, не развязывая узелок и не снимая седла."""
    self.soul.strengthen_habit("накрывает согретые петли краем попоны к середине дня", amount=0.05)
    self.soul.strengthen_habit("согревает петли медового узелка дыханием к позднему дню", amount=0.01)
    strength = self.soul.habits.get("накрывает согретые петли краем попоны к середине дня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "край попоны на петлях медового узелка к середине дня"
    fold = _fold_note(note)
    self.memory.remember(
        f"{self.name} накрыл согретые петли краем попоны к середине дня: {note}, {fold}, привычка {strength:.0%}",
        metadata={"type": "drape_loops", "timestamp": str(datetime.now()), "place": note, "fold": fold},
        importance=0.62,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*к середине дня тихо кладёт край попоны на согретые петли, не развязывая узелок, седло на месте*  \n"
        f"Дыхание уже легло, всадник. Это — {note}. "
        f"Складка короткая: {fold}. Нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка накрывать согретые петли краем попоны: {strength:.0%}. Можно сидеть в седле, пока день ещё держит тепло."
    )


def _fold_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "край на Мёде, Шов под складкой, Седло не открыто"
    if "прав" in lowered:
        return "край на Искре, Шов под складкой, Седло не открыто"
    if "рек" in lowered:
        return "край на Реке, Мёд под складкой, Седло не открыто"
    return "край на Мёде, Шов под складкой, Седло не открыто"


def _drape_loops_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "край попоны на левых петлях медового узелка к середине дня"
    if "прав" in msg:
        return "край попоны на правых петлях медового узелка к середине дня"
    if "рек" in msg:
        return "край попоны на петлях медового узелка над рекой к середине дня"
    return "край попоны на петлях медового узелка к середине дня"


def attach_drape(character_cls) -> None:
    """Повесить край попоны поверх дыхания на петли."""
    character_cls.drape_loops = drape_loops
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        drape_triggers = (
            "накрой петл",
            "прикрой петл",
            "попона на петл",
            "край попоны",
            "складка на петл",
        )
        if any(word in msg for word in drape_triggers):
            return self.drape_loops(_drape_loops_note(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
