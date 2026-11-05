"""К вечеру после зрачка: тихо положить кончик радужки на седло под тенью, седло не снимаем.

Запуск: см. examples/wednesday_evening_rest_iris_saddle.py
"""

from datetime import datetime


def rest_iris_saddle(self, place: str = "тихое положение кончика радужки на седло под тенью к вечеру") -> str:
    """После зрачка: тихо кладёт кончик радужки на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик радужки на седло под тенью к вечеру после зрачка", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик зрачка на седло под тенью к вечеру после глаза", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик радужки на седло под тенью к вечеру после зрачка", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика радужки на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик радужки на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_iris_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик радужки на седло под тенью, седло на месте*  \n"
        f"После зрачка хорошо положить кончик радужки, всадник. Это — {note}. "
        f"Тёплая радужка уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик радужки на седло под тенью к вечеру после зрачка: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _iris_place(message: str) -> str:
    msg = message.lower()
    if "радужк" in msg or "iris" in msg or "кончик" in msg:
        return "тихое положение кончика радужки на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика радужки на седло под тенью"
    return "тихое положение кончика радужки на седло под тенью к вечеру"


def attach_rest_iris_saddle(character_cls) -> None:
    """Тихо класть кончик радужки на седло под тенью к вечеру после зрачка."""
    character_cls.rest_iris_saddle = rest_iris_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        iris_triggers = (
            "положи радужку",
            "положи радужку на седло",
            "положение радужки на седло",
            "рест радужка седло",
            "положи после зрачка радужку",
        )
        if any(word in msg for word in iris_triggers):
            return self.rest_iris_saddle(_iris_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
