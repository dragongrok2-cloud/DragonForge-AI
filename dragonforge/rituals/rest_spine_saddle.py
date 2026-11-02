"""К вечеру после положения ребра крыла: тихо положить хребет на седло под тенью, седло не снимаем.

Запуск: см. examples/monday_evening_rest_spine_saddle.py
"""

from datetime import datetime


def rest_spine_saddle(self, place: str = "тихое положение хребета на седло под тенью к вечеру") -> str:
    """После ребра: тихо кладёт хребет на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт хребет на седло под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт ребро крыла на седло под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт хребет на седло под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение хребета на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт хребет на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_spine_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт хребет на седло под тенью, седло на месте*  \n"
        f"После ребра хорошо положить хребет, всадник. Это — {note}. "
        f"Тёплый хребет уютно лежит на седле, дыхание глубокое и ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть хребет на седло под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _spine_place(message: str) -> str:
    msg = message.lower()
    if "хребет" in msg or "spine" in msg or "спин" in msg:
        return "тихое положение хребета на седло"
    if "положи" in msg or "седл" in msg:
        return "положение хребета на седло под тенью"
    return "тихое положение хребета на седло под тенью к вечеру"


def attach_rest_spine_saddle(character_cls) -> None:
    """Тихо класть хребет на седло под тенью к вечеру."""
    character_cls.rest_spine_saddle = rest_spine_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        spine_triggers = (
            "положи хребет",
            "положи хребет на седло",
            "положение хребета на седло",
            "рест спайн седло",
            "положи после ребра",
        )
        if any(word in msg for word in spine_triggers):
            return self.rest_spine_saddle(_spine_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
