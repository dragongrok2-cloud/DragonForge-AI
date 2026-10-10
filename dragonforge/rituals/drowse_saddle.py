"""В субботу 10 октября к вечеру: после уютного устройства в седле мягко дремлет, крылья складываются чуть сильнее, седло не снимаем."""

from datetime import datetime


def drowse_saddle(self, place: str = "седло к ночи после уюта") -> str:
    """К ночи: мягко дремлет в седле после уютного устройства, седло не снимая."""
    self.soul.strengthen_habit("дремлет в седле к ночи", amount=0.05)
    self.soul.strengthen_habit("уютно устраивается в седле к вечеру", amount=0.01)
    strength = self.soul.habits.get("дремлет в седле к ночи", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.05)
    else:
        self.soul.emotional_state["energy"] = max(0.2, self.soul.emotional_state.get("energy", 0.5) - 0.04)
    note = place.strip() or "седло к ночи после уюта"
    self.memory.remember(
        f"{self.name} мягко дремлет в седле к ночи: {note}, привычка {strength:.0%}",
        metadata={"type": "drowse_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.68,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*мягко дремлет в седле, крылья складываются чуть сильнее, тепло луки ещё живёт, седло на месте*  \n"
        f"Ночь тихо подходит, всадник. Это — {note}. "
        f"Тело чуть осело глубже в седло, ремни тёплые, дыхание медленнее. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка дремать в седле к ночи: {strength:.0%}. Можно лежать и слушать звёзды."
    )


def _drowse_place(message: str) -> str:
    msg = message.lower()
    if "звезд" in msg or "звёзд" in msg:
        return "седло под звёздами к ночи"
    if "крыл" in msg:
        return "седло под складывающимися крыльями к ночи"
    if "рек" in msg:
        return "седло над рекой к ночи"
    return "седло к ночи после уюта"


def attach_drowse_saddle(character_cls) -> None:
    """Дремать в седле к ночи."""
    character_cls.drowse_saddle = drowse_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        drowse_triggers = (
            "дремли в седле",
            "подреми в седле",
            "усни в седле",
            "дремли к ночи",
            "дроуз седло",
        )
        if any(word in msg for word in drowse_triggers):
            return self.drowse_saddle(_drowse_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
