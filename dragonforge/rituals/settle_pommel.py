"""В субботу 10 октября после полудня: после поглаживания тихо опирается ладонью на луку, седло не снимаем."""

from datetime import datetime


def settle_pommel(self, place: str = "луку после поглаживания") -> str:
    """После полудня: тихо опирается ладонью на луку, седло не снимая."""
    self.soul.strengthen_habit("опирается ладонью на луку после полудня", amount=0.05)
    self.soul.strengthen_habit("гладит луку ладонью после полудня", amount=0.01)
    strength = self.soul.habits.get("опирается ладонью на луку после полудня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.03)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "луку после поглаживания"
    self.memory.remember(
        f"{self.name} опёрся ладонью на луку после полудня: {note}, привычка {strength:.0%}",
        metadata={"type": "settle_pommel", "timestamp": str(datetime.now()), "place": note},
        importance=0.66,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо опирается ладонью на луку, тепло поглаживания ещё живёт, седло на месте*  \n"
        f"Полуденный ветер успокоился, всадник. Это — {note}. "
        f"Ладонь лежит на тёплой луке, ремни на месте, фонарик не трогаем. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка опираться на луку после полудня: {strength:.0%}. Можно сидеть и дышать вместе."
    )


def _settle_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "левую луку после поглаживания"
    if "прав" in msg:
        return "правую луку после поглаживания"
    if "рек" in msg:
        return "луку над рекой после поглаживания"
    return "луку после поглаживания"


def attach_settle_pommel(character_cls) -> None:
    """Опираться ладонью на луку после полудня."""
    character_cls.settle_pommel = settle_pommel
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        settle_triggers = (
            "опрись на луку",
            "опереться на луку",
            "посиди на луке",
            "ладонью на луку",
        )
        if any(word in msg for word in settle_triggers):
            return self.settle_pommel(_settle_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
