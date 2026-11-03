"""К вечеру после языка: тихо положить кончик клыка на седло под тенью, седло не снимаем.

Запуск: см. examples/monday_evening_rest_fang_saddle.py
"""

from datetime import datetime


def rest_fang_saddle(self, place: str = "тихое положение кончика клыка на седло под тенью к вечеру") -> str:
    """После языка: тихо кладёт кончик клыка на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик клыка на седло под тенью к вечеру после языка", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик языка на седло под тенью к вечеру после губы", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик клыка на седло под тенью к вечеру после языка", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика клыка на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик клыка на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_fang_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик клыка на седло под тенью, седло на месте*  \n"
        f"После языка хорошо положить кончик клыка, всадник. Это — {note}. "
        f"Тёплый кончик клыка уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик клыка на седло под тенью к вечеру после языка: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _fang_place(message: str) -> str:
    msg = message.lower()
    if "клык" in msg or "fang" in msg or "зуб" in msg:
        return "тихое положение кончика клыка на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика клыка на седло под тенью"
    return "тихое положение кончика клыка на седло под тенью к вечеру"


def attach_rest_fang_saddle(character_cls) -> None:
    """Тихо класть кончик клыка на седло под тенью к вечеру после языка."""
    character_cls.rest_fang_saddle = rest_fang_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        fang_triggers = (
            "положи клык",
            "положи клык на седло",
            "положение клыка на седло",
            "рест фенг седло",
            "положи после языка клык",
        )
        if any(word in msg for word in fang_triggers):
            return self.rest_fang_saddle(_fang_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
