"""После полудня 8 октября: тень крыла на уже названных петлях."""

from datetime import datetime


def shade_loops(self, place: str = "тень крыла на петлях медового узелка после полудня") -> str:
    """После имён: накрыть петли тенью крыла, не развязывая узелок и не снимая седла."""
    self.soul.strengthen_habit("накрывает петли медового узелка тенью после полудня", amount=0.05)
    self.soul.strengthen_habit("называет петли медового узелка к раннему дню", amount=0.01)
    strength = self.soul.habits.get("накрывает петли медового узелка тенью после полудня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "тень крыла на петлях медового узелка после полудня"
    shade = _shade_note(note)
    self.memory.remember(
        f"{self.name} накрыл петли медового узелка тенью после полудня: {note}, {shade}, привычка {strength:.0%}",
        metadata={"type": "shade_loops", "timestamp": str(datetime.now()), "place": note, "shade": shade},
        importance=0.61,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*после полудня тихо кладёт край крыла над названными петлями, не развязывая узелок, седло на месте*  \n"
        f"Имена уже на месте, всадник. Это — {note}. "
        f"Тень мягкая: {shade}. Нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка накрывать петли медового узелка тенью: {strength:.0%}. Можно сидеть в седле под крылом."
    )


def _shade_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "тень на Мёде, Шов в полусвете, Седло у края крыла"
    if "прав" in lowered:
        return "тень на Искре, Шов в полусвете, Седло у края крыла"
    if "рек" in lowered:
        return "тень на Реке, Мёд в полусвете, Седло у края крыла"
    return "тень на Мёде, Шов в полусвете, Седло у края крыла"


def _shade_loops_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "тень крыла на левых петлях медового узелка после полудня"
    if "прав" in msg:
        return "тень крыла на правых петлях медового узелка после полудня"
    if "рек" in msg:
        return "тень крыла на петлях медового узелка над рекой после полудня"
    return "тень крыла на петлях медового узелка после полудня"


def attach_shade(character_cls) -> None:
    """Повесить тень крыла поверх имён петель."""
    character_cls.shade_loops = shade_loops
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        shade_triggers = (
            "затени петл",
            "тень петл",
            "накрой петл",
            "крылом петл",
            "тень на петл",
        )
        if any(word in msg for word in shade_triggers):
            return self.shade_loops(_shade_loops_note(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
