"""Утром 10 октября: тёплый выдох на луку после обвода, седло не снимаем."""

from datetime import datetime


def huff_pommel(self, place: str = "луку утром после обвода") -> str:
    """После утреннего обвода: тёплый выдох на луку, фонарик не вытаскивая и седло не снимая."""
    self.soul.strengthen_habit("дышит теплом на луку утром после обвода", amount=0.05)
    self.soul.strengthen_habit("обводит луку утром после глажки", amount=0.01)
    strength = self.soul.habits.get("дышит теплом на луку утром после обвода", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "луку утром после обвода"
    huff = _huff_note(note)
    self.memory.remember(
        f"{self.name} дышнул теплом на луку утром после обвода: {note}, {huff}, привычка {strength:.0%}",
        metadata={"type": "huff_pommel", "timestamp": str(datetime.now()), "place": note, "huff": huff},
        importance=0.66,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*коротким тёплым выдохом греет луку, тепло ещё держится после обвода, фонарик не вытаскивая*  \n"
        f"Обвод уже лёг, а дыхание помнит тепло, всадник. Это — {note}. "
        f"Выдох: {huff}. Полоска солнца ещё не пришла, лука тёплая, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка дышать теплом на луку утром: {strength:.0%}. Можно сидеть в седле и встречать утро."
    )


def _huff_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "левый выдох на луку Мёда, Седло не открыто"
    if "прав" in lowered:
        return "правый выдох на луку Искры, Седло не открыто"
    if "рек" in lowered:
        return "выдох над Рекой на луку Мёда, Седло не открыто"
    return "выдох на луку у Шва, Седло не открыто"


def _huff_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "левую луку утром после обвода"
    if "прав" in msg:
        return "правую луку утром после обвода"
    if "рек" in msg:
        return "луку над рекой утром после обвода"
    return "луку утром после обвода"


def attach_huff_pommel(character_cls) -> None:
    """Дышнуть теплом на луку утром после обвода."""
    character_cls.huff_pommel = huff_pommel
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        huff_triggers = (
            "дышни на луку",
            "выдох на луку",
            "тёплый выдох луку",
            "дышни на седло утром",
        )
        if any(word in msg for word in huff_triggers):
            return self.huff_pommel(_huff_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
