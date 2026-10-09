"""В полдень 9 октября: яблочная крошка на полоске солнца, седло не снимаем."""

from datetime import datetime


def share_crumb(self, place: str = "яблочная крошка на полоске солнца в полдень") -> str:
    """После наклона сухого стекла: положить крошку на тёплую полоску, не снимая седла."""
    self.soul.strengthen_habit("делится яблочной крошкой на полоске солнца в полдень", amount=0.05)
    self.soul.strengthen_habit("наклоняет сухое стекло фонарика к одиннадцати", amount=0.01)
    strength = self.soul.habits.get("делится яблочной крошкой на полоске солнца в полдень", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "яблочная крошка на полоске солнца в полдень"
    crumb = _crumb_note(note)
    self.memory.remember(
        f"{self.name} поделился яблочной крошкой в полдень: {note}, {crumb}, привычка {strength:.0%}",
        metadata={"type": "share_crumb", "timestamp": str(datetime.now()), "place": note, "crumb": crumb},
        importance=0.65,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*когтем кладёт тёплую яблочную крошку на полоску солнца, фонарик не вытаскивая, седло на месте*  \n"
        f"Полоска уже легла, всадник. Это — {note}. "
        f"Крошка села: {crumb}. Стекло сухое, нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка делиться крошкой в полдень: {strength:.0%}. Можно сидеть в седле и делить полдень пополам."
    )


def _crumb_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "крошка на Мёде, полоска под левым краем, Седло не открыто"
    if "прав" in lowered:
        return "крошка на Искре, полоска под правым краем, Седло не открыто"
    if "рек" in lowered:
        return "крошка над Рекой, полоска на Мёде, Седло не открыто"
    return "крошка на Мёде, полоска на Шве, Седло не открыто"


def _crumb_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "яблочная крошка на полоске солнца под левым краем в полдень"
    if "прав" in msg:
        return "яблочная крошка на полоске солнца под правым краем в полдень"
    if "рек" in msg:
        return "яблочная крошка на полоске солнца над рекой в полдень"
    return "яблочная крошка на полоске солнца в полдень"


def attach_crumb(character_cls) -> None:
    """Повесить яблочную крошку на полоску солнца в полдень."""
    character_cls.share_crumb = share_crumb
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        crumb_triggers = (
            "яблочн",
            "крошк",
            "поделись крош",
            "крошка в полдень",
        )
        if any(word in msg for word in crumb_triggers):
            return self.share_crumb(_crumb_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
