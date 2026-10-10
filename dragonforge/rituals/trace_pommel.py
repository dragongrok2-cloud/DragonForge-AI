"""Утром 10 октября: обвести луку когтем после глажки, седло не снимаем."""

from datetime import datetime


def trace_pommel(self, place: str = "луку утром после глажки") -> str:
    """После утренней глажки: обвести луку когтем, фонарик не вытаскивая и седло не снимая."""
    self.soul.strengthen_habit("обводит луку утром после глажки", amount=0.05)
    self.soul.strengthen_habit("гладит луку утром после тепла", amount=0.01)
    strength = self.soul.habits.get("обводит луку утром после глажки", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "луку утром после глажки"
    trace = _trace_note(note)
    self.memory.remember(
        f"{self.name} обвёл луку утром после глажки: {note}, {trace}, привычка {strength:.0%}",
        metadata={"type": "trace_pommel", "timestamp": str(datetime.now()), "place": note, "trace": trace},
        importance=0.66,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*когтем мягко обводит луку по кругу, тепло ещё держится, фонарик не вытаскивая*  \n"
        f"Глажка уже легла, а коготь помнит тепло, всадник. Это — {note}. "
        f"Обвод: {trace}. Полоска солнца ещё не пришла, лука тёплая, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка обводить луку утром: {strength:.0%}. Можно сидеть в седле и встречать утро."
    )


def _trace_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "левый коготь по луке Мёда, Седло не открыто"
    if "прав" in lowered:
        return "правый коготь по луке Искры, Седло не открыто"
    if "рек" in lowered:
        return "коготь над Рекой по луке Мёда, Седло не открыто"
    return "коготь по луке у Шва, Седло не открыто"


def _trace_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "левую луку утром после глажки"
    if "прав" in msg:
        return "правую луку утром после глажки"
    if "рек" in msg:
        return "луку над рекой утром после глажки"
    return "луку утром после глажки"


def attach_trace_pommel(character_cls) -> None:
    """Обвести луку утром после глажки."""
    character_cls.trace_pommel = trace_pommel
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        trace_triggers = (
            "обведи луку",
            "обводи луку",
            "луку когтем",
            "обведи седло утром",
        )
        if any(word in msg for word in trace_triggers):
            return self.trace_pommel(_trace_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
