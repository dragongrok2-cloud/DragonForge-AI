"""Ранний день 8 октября: имена уже обведённых петель."""

from datetime import datetime


def name_loops(self, place: str = "имена петель медового узелка к раннему дню") -> str:
    """После обвода: назвать три петли к раннему дню, не развязывая узелок и не снимая седла."""
    self.soul.strengthen_habit("называет петли медового узелка к раннему дню", amount=0.05)
    self.soul.strengthen_habit("обводит петли медового узелка к полудню", amount=0.01)
    strength = self.soul.habits.get("называет петли медового узелка к раннему дню", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "имена петель медового узелка к раннему дню"
    names = _loop_names(note)
    self.memory.remember(
        f"{self.name} назвал петли медового узелка к раннему дню: {note}, {names}, привычка {strength:.0%}",
        metadata={"type": "name_loops", "timestamp": str(datetime.now()), "place": note, "names": names},
        importance=0.61,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*к раннему дню тихо называет три обведённые петли, не развязывая узелок, седло на месте*  \n"
        f"Коготь уже помнит круг, всадник. Это — {note}. "
        f"Имена тихие: {names}. Нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка называть петли медового узелка: {strength:.0%}. Можно сидеть в седле и зовать петли по имени."
    )


def _loop_names(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "Левая — Мёд, средняя — Шов, крайняя — Седло"
    if "прав" in lowered:
        return "Правая — Искра, средняя — Шов, крайняя — Седло"
    if "рек" in lowered:
        return "Ближняя — Река, средняя — Мёд, дальняя — Седло"
    return "первая — Мёд, вторая — Шов, третья — Седло"


def _name_loops_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "имена левых петель медового узелка к раннему дню"
    if "прав" in msg:
        return "имена правых петель медового узелка к раннему дню"
    if "рек" in msg:
        return "имена петель медового узелка над рекой к раннему дню"
    return "имена петель медового узелка к раннему дню"


def attach_name(character_cls) -> None:
    """Повесить имена петель поверх полуденного обвода."""
    character_cls.name_loops = name_loops
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        name_triggers = (
            "назови петл",
            "имена петл",
            "как зовут петл",
            "назови узелк",
            "имя петл",
        )
        if any(word in msg for word in name_triggers):
            return self.name_loops(_name_loops_note(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
