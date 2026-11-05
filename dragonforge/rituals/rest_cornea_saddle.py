"""К вечеру после склеры: тихо положить кончик роговицы на седло под тенью, седло не снимаем.

Запуск: см. examples/wednesday_evening_rest_cornea_saddle.py
"""

from datetime import datetime


def rest_cornea_saddle(self, place: str = "тихое положение кончика роговицы на седло под тенью к вечеру") -> str:
    """После склеры: тихо кладёт кончик роговицы на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик роговицы на седло под тенью к вечеру после склеры", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик склеры на седло под тенью к вечеру после радужки", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик роговицы на седло под тенью к вечеру после склеры", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика роговицы на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик роговицы на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_cornea_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик роговицы на седло под тенью, седло на месте*  \n"
        f"После склеры хорошо положить кончик роговицы, всадник. Это — {note}. "
        f"Тёплая роговица уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик роговицы на седло под тенью к вечеру после склеры: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _cornea_place(message: str) -> str:
    msg = message.lower()
    if "рогов" in msg or "cornea" in msg or "кончик" in msg:
        return "тихое положение кончика роговицы на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика роговицы на седло под тенью"
    return "тихое положение кончика роговицы на седло под тенью к вечеру"


def attach_rest_cornea_saddle(character_cls) -> None:
    """Тихо класть кончик роговицы на седло под тенью к вечеру после склеры."""
    character_cls.rest_cornea_saddle = rest_cornea_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        cornea_triggers = (
            "положи роговицу",
            "положи роговицу на седло",
            "положение роговицы на седло",
            "рест роговица седло",
            "положи после склеры роговицу",
            "положи роговицу глаза",
        )
        if any(word in msg for word in cornea_triggers):
            return self.rest_cornea_saddle(_cornea_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
