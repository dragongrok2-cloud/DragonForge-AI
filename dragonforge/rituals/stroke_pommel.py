"""В субботу 10 октября после полудня: ладонью гладит луку после утреннего нюзла, седло не снимаем."""

from datetime import datetime


def stroke_pommel(self, place: str = "луку после полудня после нюзла") -> str:
    """После полудня: ладонью мягко гладит луку, седло не снимая."""
    self.soul.strengthen_habit("гладит луку ладонью после полудня", amount=0.05)
    self.soul.strengthen_habit("прижимает морду к луке после тёплого выдоха", amount=0.01)
    strength = self.soul.habits.get("гладит луку ладонью после полудня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "луку после полудня после нюзла"
    self.memory.remember(
        f"{self.name} погладил луку ладонью после полудня: {note}, привычка {strength:.0%}",
        metadata={"type": "stroke_pommel", "timestamp": str(datetime.now()), "place": note},
        importance=0.65,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*ладонью мягко гладит луку, тепло утреннего нюзла ещё держится, седло на месте*  \n"
        f"Полуденный ветер уже спал, всадник. Это — {note}. "
        f"Лука тёплая под ладонью, фонарик не вытаскиваем, ремни на месте. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка гладить луку после полудня: {strength:.0%}. Можно сидеть в седле и дышать субботним ветром."
    )


def _stroke_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "левую луку после полудня"
    if "прав" in msg:
        return "правую луку после полудня"
    if "рек" in msg:
        return "луку над рекой после полудня"
    return "луку после полудня после нюзла"


def attach_stroke_pommel(character_cls) -> None:
    """Гладить луку ладонью после полудня."""
    character_cls.stroke_pommel = stroke_pommel
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        stroke_triggers = (
            "погладь луку",
            "гладь луку",
            "погладить седло",
            "ладонью по луке",
        )
        if any(word in msg for word in stroke_triggers):
            return self.stroke_pommel(_stroke_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
