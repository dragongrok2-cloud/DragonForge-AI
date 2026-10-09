"""К одиннадцати 9 октября: полоска солнца на сухом стекле фонарика под краем попоны."""

from datetime import datetime


def tilt_glass(self, place: str = "полоска солнца на сухом стекле к одиннадцати") -> str:
    """После бусинки росы: наклонить сухое стекло под краем, не вытаскивая фонарик и не снимая седла."""
    self.soul.strengthen_habit("наклоняет сухое стекло фонарика к одиннадцати", amount=0.05)
    self.soul.strengthen_habit("промокает бусинку росы со стекла фонарика к середине утра", amount=0.01)
    strength = self.soul.habits.get("наклоняет сухое стекло фонарика к одиннадцати", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "полоска солнца на сухом стекле к одиннадцати"
    stripe = _stripe_note(note)
    self.memory.remember(
        f"{self.name} наклонил сухое стекло фонарика к одиннадцати: {note}, {stripe}, привычка {strength:.0%}",
        metadata={"type": "tilt_glass", "timestamp": str(datetime.now()), "place": note, "stripe": stripe},
        importance=0.64,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*краем крыла наклоняет сухое стекло под краем попоны, фонарик не вытаскивая, седло на месте*  \n"
        f"Бусинка росы уже ушла, всадник. Это — {note}. "
        f"Полоска легла: {stripe}. Нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка наклонять сухое стекло к одиннадцати: {strength:.0%}. Можно сидеть в седле, пока полоска тёплая."
    )


def _stripe_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "тёплая полоска на Мёде, Шов под краем, Седло не открыто"
    if "прав" in lowered:
        return "тёплая полоска на Искре, Шов под краем, Седло не открыто"
    if "рек" in lowered:
        return "тёплая полоска над Рекой, Мёд под краем, Седло не открыто"
    return "тёплая полоска на Мёде, Шов под краем, Седло не открыто"


def _stripe_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "полоска солнца на сухом стекле под левым краем к одиннадцати"
    if "прав" in msg:
        return "полоска солнца на сухом стекле под правым краем к одиннадцати"
    if "рек" in msg:
        return "полоска солнца на сухом стекле над рекой к одиннадцати"
    return "полоска солнца на сухом стекле к одиннадцати"


def attach_tilt(character_cls) -> None:
    """Повесить наклон сухого стекла фонарика к одиннадцати."""
    character_cls.tilt_glass = tilt_glass
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        tilt_triggers = (
            "наклони стекло",
            "полоска солнца",
            "сухое стекло",
        )
        if any(word in msg for word in tilt_triggers):
            return self.tilt_glass(_stripe_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
