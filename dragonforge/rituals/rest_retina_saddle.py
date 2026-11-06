"""К вечеру после хрусталика: тихо положить кончик сетчатки на седло под тенью, седло не снимаем.

Запуск: см. examples/wednesday_evening_rest_retina_saddle.py
"""

from datetime import datetime


def rest_retina_saddle(self, place: str = "тихое положение кончика сетчатки на седло под тенью к вечеру") -> str:
    """После хрусталика: тихо кладёт кончик сетчатки на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик сетчатки на седло под тенью к вечеру после хрусталика", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик хрусталика на седло под тенью к вечеру после роговицы", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик сетчатки на седло под тенью к вечеру после хрусталика", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика сетчатки на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик сетчатки на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_retina_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик сетчатки на седло под тенью, седло на месте*  \n"
        f"После хрусталика хорошо положить кончик сетчатки, всадник. Это — {note}. "
        f"Тёплая сетчатка уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик сетчатки на седло под тенью к вечеру после хрусталика: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _retina_place(message: str) -> str:
    msg = message.lower()
    if "сетчат" in msg or "retina" in msg or "кончик" in msg:
        return "тихое положение кончика сетчатки на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика сетчатки на седло под тенью"
    return "тихое положение кончика сетчатки на седло под тенью к вечеру"


def attach_rest_retina_saddle(character_cls) -> None:
    """Тихо класть кончик сетчатки на седло под тенью к вечеру после хрусталика."""
    character_cls.rest_retina_saddle = rest_retina_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        retina_triggers = (
            "положи сетчатку",
            "положи сетчатку на седло",
            "положение сетчатки на седло",
            "рест сетчатка седло",
            "положи после хрусталика сетчатку",
            "положи сетчатку глаза",
        )
        if any(word in msg for word in retina_triggers):
            return self.rest_retina_saddle(_retina_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
