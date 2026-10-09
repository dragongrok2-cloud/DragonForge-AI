"""Утром 9 октября: ладони о стекло фонарика под краем попоны."""

from datetime import datetime


def cup_glow(self, place: str = "ладони о стекло фонарика под краем попоны утром") -> str:
    """После вечернего фонарика: согреть ладони о стекло, не вытаскивая его и не снимая седла."""
    self.soul.strengthen_habit("согревает ладони о стекло фонарика под краем утром", amount=0.05)
    self.soul.strengthen_habit("подтыкает фонарик под разглаженный край попоны к вечеру", amount=0.01)
    strength = self.soul.habits.get("согревает ладони о стекло фонарика под краем утром", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "ладони о стекло фонарика под краем попоны утром"
    warmth = _warmth_note(note)
    self.memory.remember(
        f"{self.name} согрел ладони о стекло фонарика утром: {note}, {warmth}, привычка {strength:.0%}",
        metadata={"type": "cup_glow", "timestamp": str(datetime.now()), "place": note, "warmth": warmth},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*утром тихо складывает ладони о стекло фонарика под краем, не вытаскивая его, седло на месте*  \n"
        f"Фонарик уже лежит, всадник. Это — {note}. "
        f"Тепло короткое: {warmth}. Нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка согревать ладони о стекло утром: {strength:.0%}. Можно сидеть в седле, пока стекло ещё тёплое."
    )


def _warmth_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "тепло на Мёде, Шов под краем, Седло не открыто"
    if "прав" in lowered:
        return "тепло на Искре, Шов под краем, Седло не открыто"
    if "рек" in lowered:
        return "тепло над Рекой, Мёд под краем, Седло не открыто"
    return "тепло на Мёде, Шов под краем, Седло не открыто"


def _glow_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "ладони о стекло фонарика под левым краем утром"
    if "прав" in msg:
        return "ладони о стекло фонарика под правым краем утром"
    if "рек" in msg:
        return "ладони о стекло фонарика над рекой утром"
    return "ладони о стекло фонарика под краем попоны утром"


def attach_cup(character_cls) -> None:
    """Повесить утренние ладони на стекло фонарика под краем."""
    character_cls.cup_glow = cup_glow
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        glow_triggers = (
            "согрей ладони",
            "ладони о стекло",
            "стекло фонарика",
            "чаша света",
            "согрей стекло",
        )
        if any(word in msg for word in glow_triggers):
            return self.cup_glow(_glow_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
