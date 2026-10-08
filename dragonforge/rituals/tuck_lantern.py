"""К вечеру 8 октября: фонарик под уже разглаженный край попоны."""

from datetime import datetime


def tuck_lantern(self, place: str = "фонарик под разглаженный край попоны к вечеру") -> str:
    """После ладони по краю: подсунуть маленький фонарик, не развязывая узелок и не снимая седла."""
    self.soul.strengthen_habit("подтыкает фонарик под разглаженный край попоны к вечеру", amount=0.05)
    self.soul.strengthen_habit("гладит край попоны на согретых петлях к вечеру", amount=0.01)
    strength = self.soul.habits.get("подтыкает фонарик под разглаженный край попоны к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "фонарик под разглаженный край попоны к вечеру"
    glow = _glow_note(note)
    self.memory.remember(
        f"{self.name} подсунул фонарик под край попоны к вечеру: {note}, {glow}, привычка {strength:.0%}",
        metadata={"type": "tuck_lantern", "timestamp": str(datetime.now()), "place": note, "glow": glow},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*к вечеру тихо подтыкает фонарик под разглаженный край попоны, не развязывая узелок, седло на месте*  \n"
        f"Край уже гладкий, всадник. Это — {note}. "
        f"Свет короткий: {glow}. Нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка подтыкать фонарик под край к вечеру: {strength:.0%}. Можно сидеть в седле, пока свет ещё тёплый."
    )


def _glow_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "свет на Мёде, Шов под краем, Седло не открыто"
    if "прав" in lowered:
        return "свет на Искре, Шов под краем, Седло не открыто"
    if "рек" in lowered:
        return "свет над Рекой, Мёд под краем, Седло не открыто"
    return "свет на Мёде, Шов под краем, Седло не открыто"


def _lantern_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "фонарик под левый край попоны к вечеру"
    if "прав" in msg:
        return "фонарик под правый край попоны к вечеру"
    if "рек" in msg:
        return "фонарик под край попоны над рекой к вечеру"
    return "фонарик под разглаженный край попоны к вечеру"


def attach_lantern(character_cls) -> None:
    """Повесить вечерний фонарик под разглаженный край попоны."""
    character_cls.tuck_lantern = tuck_lantern
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        lantern_triggers = (
            "подсунь фонарик",
            "подтыкай фонарик",
            "фонарик под край",
            "фонарик под попону",
            "свет под попону",
        )
        if any(word in msg for word in lantern_triggers):
            return self.tuck_lantern(_lantern_note(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
