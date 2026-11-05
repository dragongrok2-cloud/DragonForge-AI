"""К вечеру после радужки: тихо положить кончик склеры на седло под тенью, седло не снимаем.

Запуск: см. examples/wednesday_evening_rest_sclera_saddle.py
"""

from datetime import datetime


def rest_sclera_saddle(self, place: str = "тихое положение кончика склеры на седло под тенью к вечеру") -> str:
    """После радужки: тихо кладёт кончик склеры на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик склеры на седло под тенью к вечеру после радужки", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик радужки на седло под тенью к вечеру после зрачка", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик склеры на седло под тенью к вечеру после радужки", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика склеры на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик склеры на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_sclera_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик склеры на седло под тенью, седло на месте*  \n"
        f"После радужки хорошо положить кончик склеры, всадник. Это — {note}. "
        f"Тёплая склера уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик склеры на седло под тенью к вечеру после радужки: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _sclera_place(message: str) -> str:
    msg = message.lower()
    if "склер" in msg or "sclera" in msg or "кончик" in msg or "белок" in msg:
        return "тихое положение кончика склеры на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика склеры на седло под тенью"
    return "тихое положение кончика склеры на седло под тенью к вечеру"


def attach_rest_sclera_saddle(character_cls) -> None:
    """Тихо класть кончик склеры на седло под тенью к вечеру после радужки."""
    character_cls.rest_sclera_saddle = rest_sclera_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        sclera_triggers = (
            "положи склеру",
            "положи склеру на седло",
            "положение склеры на седло",
            "рест склера седло",
            "положи после радужки склеру",
            "положи белок",
            "положи белок глаза",
        )
        if any(word in msg for word in sclera_triggers):
            return self.rest_sclera_saddle(_sclera_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
