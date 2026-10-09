"""К середине утра 9 октября: бусинка росы со стекла фонарика под краем попоны."""

from datetime import datetime


def blot_bead(self, place: str = "бусинка росы со стекла фонарика к середине утра") -> str:
    """После утренних ладоней: промокнуть бусинку росы краем крыла, не вытаскивая фонарик и не снимая седла."""
    self.soul.strengthen_habit("промокает бусинку росы со стекла фонарика к середине утра", amount=0.05)
    self.soul.strengthen_habit("согревает ладони о стекло фонарика под краем утром", amount=0.01)
    strength = self.soul.habits.get("промокает бусинку росы со стекла фонарика к середине утра", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "бусинка росы со стекла фонарика к середине утра"
    bead = _bead_note(note)
    self.memory.remember(
        f"{self.name} промокнул бусинку росы со стекла фонарика к середине утра: {note}, {bead}, привычка {strength:.0%}",
        metadata={"type": "blot_bead", "timestamp": str(datetime.now()), "place": note, "bead": bead},
        importance=0.64,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*краем крыла промокает бусинку росы со стекла, фонарик не вытаскивая, седло на месте*  \n"
        f"Ладони уже согрели стекло, всадник. Это — {note}. "
        f"Капля ушла: {bead}. Нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка промокать бусинку росы к середине утра: {strength:.0%}. Можно сидеть в седле, пока стекло сухое."
    )


def _bead_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "сухо на Мёде, Шов под краем, Седло не открыто"
    if "прав" in lowered:
        return "сухо на Искре, Шов под краем, Седло не открыто"
    if "рек" in lowered:
        return "сухо над Рекой, Мёд под краем, Седло не открыто"
    return "сухо на Мёде, Шов под краем, Седло не открыто"


def _bead_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "бусинка росы со стекла фонарика под левым краем к середине утра"
    if "прав" in msg:
        return "бусинка росы со стекла фонарика под правым краем к середине утра"
    if "рек" in msg:
        return "бусинка росы со стекла фонарика над рекой к середине утра"
    return "бусинка росы со стекла фонарика к середине утра"


def attach_bead(character_cls) -> None:
    """Повесить промокание бусинки росы со стекла фонарика."""
    character_cls.blot_bead = blot_bead
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        bead_triggers = (
            "промокни бусинку",
            "бусинка росы",
            "роса со стекла",
            "промокни стекло",
        )
        if any(word in msg for word in bead_triggers):
            return self.blot_bead(_bead_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
