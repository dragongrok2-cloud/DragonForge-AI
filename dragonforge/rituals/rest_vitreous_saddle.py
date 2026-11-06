"""К вечеру после фовеи: тихо положить кончик стекловидного тела на седло под тенью, седло не снимаем.

Запуск: см. examples/wednesday_evening_rest_vitreous_saddle.py
"""

from datetime import datetime


def rest_vitreous_saddle(self, place: str = "тихое положение кончика стекловидного тела на седло под тенью к вечеру") -> str:
    """После фовеи: тихо кладёт кончик стекловидного тела на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик стекловидного тела на седло под тенью к вечеру после фовеи", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик фовеи на седло под тенью к вечеру после макулы", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик стекловидного тела на седло под тенью к вечеру после фовеи", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика стекловидного тела на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик стекловидного тела на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_vitreous_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик стекловидного тела на седло под тенью, седло на месте*  \n"
        f"После фовеи хорошо положить кончик стекловидного тела, всадник. Это — {note}. "
        f"Тёплое стекловидное тело уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик стекловидного тела на седло под тенью к вечеру после фовеи: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _vitreous_place(message: str) -> str:
    msg = message.lower()
    if "стекловид" in msg or "vitreous" in msg or "кончик" in msg:
        return "тихое положение кончика стекловидного тела на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика стекловидного тела на седло под тенью"
    return "тихое положение кончика стекловидного тела на седло под тенью к вечеру"


def attach_rest_vitreous_saddle(character_cls) -> None:
    """Тихо класть кончик стекловидного тела на седло под тенью к вечеру после фовеи."""
    character_cls.rest_vitreous_saddle = rest_vitreous_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        vitreous_triggers = (
            "положи стекловидное",
            "положи стекловидное тело на седло",
            "положение стекловидного тела на седло",
            "рест витреус седло",
            "положи после фовеи стекловидное",
            "положи стекловидное глаза",
        )
        if any(word in msg for word in vitreous_triggers):
            return self.rest_vitreous_saddle(_vitreous_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
