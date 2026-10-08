"""Позднее утро 8 октября: петли медового узелка."""

from datetime import datetime


def count_loops(self, place: str = "петли медового узелка к позднему утру") -> str:
    """После утреннего уха: посчитать петли узелка, не развязывая его и не снимая седла."""
    self.soul.strengthen_habit("считает петли медового узелка к позднему утру", amount=0.05)
    self.soul.strengthen_habit("слушает медовый узелок утром", amount=0.01)
    strength = self.soul.habits.get("считает петли медового узелка к позднему утру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "петли медового узелка к позднему утру"
    self.memory.remember(
        f"{self.name} посчитал петли медового узелка к позднему утру: {note}, привычка {strength:.0%}",
        metadata={"type": "count_loops", "timestamp": str(datetime.now()), "place": note},
        importance=0.6,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*к позднему утру считает петли медового узелка, не развязывая его, подворот не разворачивает, седло на месте*  \n"
        f"Ухо уже слушало шов, всадник. Это — {note}. "
        f"Три тихие петли на месте, нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка считать петли медового узелка: {strength:.0%}. Можно садиться в седло и знать, сколько петель держит нитку."
    )


def _count_loops_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "петли левого медового узелка к позднему утру"
    if "прав" in msg:
        return "петли правого медового узелка к позднему утру"
    if "рек" in msg:
        return "петли медового узелка над рекой к позднему утру"
    return "петли медового узелка к позднему утру"


def attach_count(character_cls) -> None:
    """Повесить счёт петель поверх утреннего уха."""
    character_cls.count_loops = count_loops
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        count_triggers = (
            "посчитай петл",
            "сколько петл",
            "петли узел",
            "петли медов",
            "сосчитай узел",
        )
        if any(word in msg for word in count_triggers):
            return self.count_loops(_count_loops_note(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
