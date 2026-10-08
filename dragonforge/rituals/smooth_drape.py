"""К вечеру 8 октября: ладонь по краю попоны на уже накрытых петлях."""

from datetime import datetime


def smooth_drape(self, place: str = "край попоны на петлях медового узелка к вечеру") -> str:
    """После края попоны: разгладить складку ладонью, не развязывая узелок и не снимая седла."""
    self.soul.strengthen_habit("гладит край попоны на согретых петлях к вечеру", amount=0.05)
    self.soul.strengthen_habit("накрывает согретые петли краем попоны к середине дня", amount=0.01)
    strength = self.soul.habits.get("гладит край попоны на согретых петлях к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "край попоны на петлях медового узелка к вечеру"
    palm = _palm_note(note)
    self.memory.remember(
        f"{self.name} разгладил край попоны к вечеру: {note}, {palm}, привычка {strength:.0%}",
        metadata={"type": "smooth_drape", "timestamp": str(datetime.now()), "place": note, "palm": palm},
        importance=0.62,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*к вечеру тихо ведёт ладонь по краю попоны, не развязывая узелок, седло на месте*  \n"
        f"Край уже лежит, всадник. Это — {note}. "
        f"Ладонь короткая: {palm}. Нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка гладить край попоны к вечеру: {strength:.0%}. Можно сидеть в седле, пока вечер ещё тёплый."
    )


def _palm_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "ладонь по Мёду, Шов под краем, Седло не открыто"
    if "прав" in lowered:
        return "ладонь по Искре, Шов под краем, Седло не открыто"
    if "рек" in lowered:
        return "ладонь над Рекой, Мёд под краем, Седло не открыто"
    return "ладонь по Мёду, Шов под краем, Седло не открыто"


def _smooth_drape_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "край попоны на левых петлях медового узелка к вечеру"
    if "прав" in msg:
        return "край попоны на правых петлях медового узелка к вечеру"
    if "рек" in msg:
        return "край попоны на петлях медового узелка над рекой к вечеру"
    return "край попоны на петлях медового узелка к вечеру"


def attach_smooth(character_cls) -> None:
    """Повесить вечернюю ладонь поверх края попоны."""
    character_cls.smooth_drape = smooth_drape
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        smooth_triggers = (
            "погладь край попоны",
            "разгладь попону",
            "погладь попону",
            "ладонь по краю",
            "край попоны вечером",
        )
        if any(word in msg for word in smooth_triggers):
            return self.smooth_drape(_smooth_drape_note(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
