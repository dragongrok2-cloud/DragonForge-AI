"""К вечеру после глаза: тихо положить кончик зрачка на седло под тенью, седло не снимаем.

Запуск: см. examples/wednesday_evening_rest_pupil_saddle.py
"""

from datetime import datetime


def rest_pupil_saddle(self, place: str = "тихое положение кончика зрачка на седло под тенью к вечеру") -> str:
    """После глаза: тихо кладёт кончик зрачка на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик зрачка на седло под тенью к вечеру после глаза", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик глаза на седло под тенью к вечеру после виска", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик зрачка на седло под тенью к вечеру после глаза", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика зрачка на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик зрачка на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_pupil_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик зрачка на седло под тенью, седло на месте*  \n"
        f"После глаза хорошо положить кончик зрачка, всадник. Это — {note}. "
        f"Тёплый зрачок уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик зрачка на седло под тенью к вечеру после глаза: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _pupil_place(message: str) -> str:
    msg = message.lower()
    if "зрачок" in msg or "pupil" in msg or "кончик" in msg:
        return "тихое положение кончика зрачка на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика зрачка на седло под тенью"
    return "тихое положение кончика зрачка на седло под тенью к вечеру"


def attach_rest_pupil_saddle(character_cls) -> None:
    """Тихо класть кончик зрачка на седло под тенью к вечеру после глаза."""
    character_cls.rest_pupil_saddle = rest_pupil_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        pupil_triggers = (
            "положи зрачок",
            "положи зрачок на седло",
            "положение зрачка на седло",
            "рест зрачок седло",
            "положи после глаза зрачок",
        )
        if any(word in msg for word in pupil_triggers):
            return self.rest_pupil_saddle(_pupil_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
