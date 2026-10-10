"""Утром 10 октября: погладить луку после вчерашнего тепла, седло не снимаем."""

from datetime import datetime


def pat_pommel(self, place: str = "луку утром после тепла") -> str:
    """После вчерашнего тепла: мягко погладить луку, фонарик не вытаскивая и седло не снимая."""
    self.soul.strengthen_habit("гладит луку утром после тепла", amount=0.05)
    self.soul.strengthen_habit("кладёт тепло сгиба на луку к вечеру", amount=0.01)
    strength = self.soul.habits.get("гладит луку утром после тепла", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "луку утром после тепла"
    pat = _pat_note(note)
    self.memory.remember(
        f"{self.name} погладил луку утром после тепла: {note}, {pat}, привычка {strength:.0%}",
        metadata={"type": "pat_pommel", "timestamp": str(datetime.now()), "place": note, "pat": pat},
        importance=0.66,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*мягко гладит луку ладонью один раз, тепло ещё держится, фонарик не вытаскивая*  \n"
        f"Вчерашнее тепло ещё на коже луки, всадник. Это — {note}. "
        f"Гладь: {pat}. Полоска солнца ещё не пришла, лука тёплая, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка гладить луку утром: {strength:.0%}. Можно сидеть в седле и встречать утро."
    )


def _pat_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "левая ладонь по луке Мёда, Седло не открыто"
    if "прав" in lowered:
        return "правая ладонь по луке Искры, Седло не открыто"
    if "рек" in lowered:
        return "ладонь над Рекой по луке Мёда, Седло не открыто"
    return "ладонь по луке у Шва, Седло не открыто"


def _pat_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "левую луку утром после тепла"
    if "прав" in msg:
        return "правую луку утром после тепла"
    if "рек" in msg:
        return "луку над рекой утром после тепла"
    return "луку утром после тепла"


def attach_pat_pommel(character_cls) -> None:
    """Погладить луку утром после вчерашнего тепла."""
    character_cls.pat_pommel = pat_pommel
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        pat_triggers = (
            "погладь луку",
            "гладь луку",
            "луку утром",
            "погладь седло утром",
        )
        if any(word in msg for word in pat_triggers):
            return self.pat_pommel(_pat_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
