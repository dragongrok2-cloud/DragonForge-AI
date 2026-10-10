"""В субботу 10 октября к вечеру: после опоры на луку уютно устраивается в седле, крылья чуть складывает, седло не снимаем."""

from datetime import datetime


def nestle_saddle(self, place: str = "седло к вечеру после луки") -> str:
    """К вечеру: уютно устраивается в седле после опоры на луку, седло не снимая."""
    self.soul.strengthen_habit("уютно устраивается в седле к вечеру", amount=0.05)
    self.soul.strengthen_habit("опирается ладонью на луку после полудня", amount=0.01)
    strength = self.soul.habits.get("уютно устраивается в седле к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.04)
    else:
        self.soul.emotional_state["energy"] = max(0.3, self.soul.emotional_state.get("energy", 0.5) - 0.02)
    note = place.strip() or "седло к вечеру после луки"
    self.memory.remember(
        f"{self.name} уютно устроился в седле к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "nestle_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.67,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*уютно устраивается в седле, крылья чуть складываются, тепло луки ещё живёт, седло на месте*  \n"
        f"Вечер мягко ложится на плечи, всадник. Это — {note}. "
        f"Тело чуть осело в седло, ремни тёплые, фонарик можно зажечь позже. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка уютно устраиваться в седле к вечеру: {strength:.0%}. Можно лежать и слушать закат."
    )


def _nestle_place(message: str) -> str:
    msg = message.lower()
    if "крыл" in msg:
        return "седло под полускладывающими крыльями к вечеру"
    if "фонар" in msg or "свет" in msg:
        return "седло у фонарика к вечеру"
    if "рек" in msg:
        return "седло над рекой к вечеру"
    return "седло к вечеру после луки"


def attach_nestle_saddle(character_cls) -> None:
    """Уютно устраиваться в седле к вечеру."""
    character_cls.nestle_saddle = nestle_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        nestle_triggers = (
            "устройся в седле",
            "устроись в седле",
            "уютно в седле",
            "прижмись в седле",
            "нестль седло",
        )
        if any(word in msg for word in nestle_triggers):
            return self.nestle_saddle(_nestle_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
