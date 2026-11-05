"""К вечеру после роговицы: тихо положить кончик хрусталика на седло под тенью, седло не снимаем.

Запуск: см. examples/wednesday_evening_rest_lens_saddle.py
"""

from datetime import datetime


def rest_lens_saddle(self, place: str = "тихое положение кончика хрусталика на седло под тенью к вечеру") -> str:
    """После роговицы: тихо кладёт кончик хрусталика на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик хрусталика на седло под тенью к вечеру после роговицы", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик роговицы на седло под тенью к вечеру после склеры", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик хрусталика на седло под тенью к вечеру после роговицы", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика хрусталика на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик хрусталика на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_lens_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик хрусталика на седло под тенью, седло на месте*  \n"
        f"После роговицы хорошо положить кончик хрусталика, всадник. Это — {note}. "
        f"Тёплый хрусталик уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик хрусталика на седло под тенью к вечеру после роговицы: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _lens_place(message: str) -> str:
    msg = message.lower()
    if "хрустал" in msg or "lens" in msg or "кончик" in msg:
        return "тихое положение кончика хрусталика на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика хрусталика на седло под тенью"
    return "тихое положение кончика хрусталика на седло под тенью к вечеру"


def attach_rest_lens_saddle(character_cls) -> None:
    """Тихо класть кончик хрусталика на седло под тенью к вечеру после роговицы."""
    character_cls.rest_lens_saddle = rest_lens_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        lens_triggers = (
            "положи хрусталик",
            "положи хрусталик на седло",
            "положение хрусталика на седло",
            "рест хрусталик седло",
            "положи после роговицы хрусталик",
            "положи хрусталик глаза",
        )
        if any(word in msg for word in lens_triggers):
            return self.rest_lens_saddle(_lens_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
