"""После полудня 9 октября: смахнуть крошку с полоски солнца, седло не снимаем."""

from datetime import datetime


def sweep_crumb(self, place: str = "крошка с полоски солнца после полудня") -> str:
    """После дележа крошки: смахнуть пыльцу крылом, не снимая седла и не вытаскивая фонарик."""
    self.soul.strengthen_habit("смахивает крошку с полоски солнца после полудня", amount=0.05)
    self.soul.strengthen_habit("делится яблочной крошкой на полоске солнца в полдень", amount=0.01)
    strength = self.soul.habits.get("смахивает крошку с полоски солнца после полудня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.01)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "крошка с полоски солнца после полудня"
    dust = _sweep_note(note)
    self.memory.remember(
        f"{self.name} смахнул крошку с полоски после полудня: {note}, {dust}, привычка {strength:.0%}",
        metadata={"type": "sweep_crumb", "timestamp": str(datetime.now()), "place": note, "dust": dust},
        importance=0.64,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*краем крыла смахивает яблочную пыльцу с полоски солнца, фонарик не вытаскивая, седло на месте*  \n"
        f"Крошка уже была поделена, всадник. Это — {note}. "
        f"Пыльца ушла: {dust}. Стекло сухое, нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка смахивать крошку после полудня: {strength:.0%}. Можно сидеть в седле и смотреть, как полоска светлеет."
    )


def _sweep_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "пыльца с Мёда, полоска под левым краем, Седло не открыто"
    if "прав" in lowered:
        return "пыльца с Искры, полоска под правым краем, Седло не открыто"
    if "рек" in lowered:
        return "пыльца над Рекой, полоска на Мёде, Седло не открыто"
    return "пыльца с Мёда, полоска на Шве, Седло не открыто"


def _sweep_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "крошка с полоски солнца под левым краем после полудня"
    if "прав" in msg:
        return "крошка с полоски солнца под правым краем после полудня"
    if "рек" in msg:
        return "крошка с полоски солнца над рекой после полудня"
    return "крошка с полоски солнца после полудня"


def attach_sweep(character_cls) -> None:
    """Повесить смахивание крошки с полоски солнца после полудня."""
    character_cls.sweep_crumb = sweep_crumb
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        sweep_triggers = (
            "смахни",
            "смети крош",
            "крошку с полоск",
            "пыльц",
        )
        if any(word in msg for word in sweep_triggers):
            return self.sweep_crumb(_sweep_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
