"""К вечеру после губы: тихо положить кончик языка на седло под тенью, седло не снимаем.

Запуск: см. examples/monday_evening_rest_tongue_saddle.py
"""

from datetime import datetime


def rest_tongue_saddle(self, place: str = "тихое положение кончика языка на седло под тенью к вечеру") -> str:
    """После губы: тихо кладёт кончик языка на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик языка на седло под тенью к вечеру после губы", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт губу на седло под тенью к вечеру после ноздри", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик языка на седло под тенью к вечеру после губы", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика языка на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик языка на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_tongue_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик языка на седло под тенью, седло на месте*  \n"
        f"После губы хорошо положить кончик языка, всадник. Это — {note}. "
        f"Тёплый кончик языка уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик языка на седло под тенью к вечеру после губы: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _tongue_place(message: str) -> str:
    msg = message.lower()
    if "язык" in msg or "tongue" in msg or "кончик" in msg:
        return "тихое положение кончика языка на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика языка на седло под тенью"
    return "тихое положение кончика языка на седло под тенью к вечеру"


def attach_rest_tongue_saddle(character_cls) -> None:
    """Тихо класть кончик языка на седло под тенью к вечеру после губы."""
    character_cls.rest_tongue_saddle = rest_tongue_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        tongue_triggers = (
            "положи язык",
            "положи язык на седло",
            "положение языка на седло",
            "рест тонг седло",
            "положи после губы язык",
        )
        if any(word in msg for word in tongue_triggers):
            return self.rest_tongue_saddle(_tongue_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
