"""К вечеру после сетчатки: тихо положить кончик макулы на седло под тенью, седло не снимаем.

Запуск: см. examples/wednesday_evening_rest_macula_saddle.py
"""

from datetime import datetime


def rest_macula_saddle(self, place: str = "тихое положение кончика макулы на седло под тенью к вечеру") -> str:
    """После сетчатки: тихо кладёт кончик макулы на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик макулы на седло под тенью к вечеру после сетчатки", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик сетчатки на седло под тенью к вечеру после хрусталика", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик макулы на седло под тенью к вечеру после сетчатки", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика макулы на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик макулы на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_macula_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик макулы на седло под тенью, седло на месте*  \n"
        f"После сетчатки хорошо положить кончик макулы, всадник. Это — {note}. "
        f"Тёплая макула уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик макулы на седло под тенью к вечеру после сетчатки: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _macula_place(message: str) -> str:
    msg = message.lower()
    if "макул" in msg or "macula" in msg or "кончик" in msg:
        return "тихое положение кончика макулы на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика макулы на седло под тенью"
    return "тихое положение кончика макулы на седло под тенью к вечеру"


def attach_rest_macula_saddle(character_cls) -> None:
    """Тихо класть кончик макулы на седло под тенью к вечеру после сетчатки."""
    character_cls.rest_macula_saddle = rest_macula_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        macula_triggers = (
            "положи макулу",
            "положи макулу на седло",
            "положение макулы на седло",
            "рест макула седло",
            "положи после сетчатки макулу",
            "положи макулу глаза",
        )
        if any(word in msg for word in macula_triggers):
            return self.rest_macula_saddle(_macula_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
