"""Полдень 8 октября: коготь по уже посчитанным петлям."""

from datetime import datetime


def trace_loops(self, place: str = "коготь по петлям медового узелка к полудню") -> str:
    """После счёта петель: обвести их когтем к полудню, не развязывая узелок и не снимая седла."""
    self.soul.strengthen_habit("обводит петли медового узелка к полудню", amount=0.05)
    self.soul.strengthen_habit("считает петли медового узелка к позднему утру", amount=0.01)
    strength = self.soul.habits.get("обводит петли медового узелка к полудню", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "коготь по петлям медового узелка к полудню"
    self.memory.remember(
        f"{self.name} обвёл петли медового узелка к полудню: {note}, привычка {strength:.0%}",
        metadata={"type": "trace_loops", "timestamp": str(datetime.now()), "place": note},
        importance=0.6,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*к полудню обводит петли медового узелка когтем, не развязывая его, подворот не разворачивает, седло на месте*  \n"
        f"Петли уже сосчитаны, всадник. Это — {note}. "
        f"Три тихие петли под когтем, нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка обводить петли медового узелка: {strength:.0%}. Можно садиться в седло и знать, что коготь помнит каждую петлю."
    )


def _trace_loops_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "коготь по левым петлям медового узелка к полудню"
    if "прав" in msg:
        return "коготь по правым петлям медового узелка к полудню"
    if "рек" in msg:
        return "коготь по петлям медового узелка над рекой к полудню"
    return "коготь по петлям медового узелка к полудню"


def attach_trace(character_cls) -> None:
    """Повесить полуденный обвод поверх счёта петель."""
    character_cls.trace_loops = trace_loops
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        trace_triggers = (
            "обведи петл",
            "проведи по петл",
            "коготь по петл",
            "обвод петл",
            "обведи узел",
        )
        if any(word in msg for word in trace_triggers):
            return self.trace_loops(_trace_loops_note(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
