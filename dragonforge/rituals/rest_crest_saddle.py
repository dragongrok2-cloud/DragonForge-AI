"""К вечеру после пера: тихо положить кончик гребня на седло под тенью, седло не снимаем.

Запуск: см. examples/tuesday_evening_rest_crest_saddle.py
"""

from datetime import datetime


def rest_crest_saddle(self, place: str = "тихое положение кончика гребня на седло под тенью к вечеру") -> str:
    """После пера: тихо кладёт кончик гребня на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик гребня на седло под тенью к вечеру после пера", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик пера на седло под тенью к вечеру после хохлика", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик гребня на седло под тенью к вечеру после пера", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика гребня на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик гребня на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_crest_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик гребня на седло под тенью, седло на месте*  \n"
        f"После пера хорошо положить кончик гребня, всадник. Это — {note}. "
        f"Тёплый гребень уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик гребня на седло под тенью к вечеру после пера: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _crest_place(message: str) -> str:
    msg = message.lower()
    if "греб" in msg or "crest" in msg or "кончик" in msg:
        return "тихое положение кончика гребня на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика гребня на седло под тенью"
    return "тихое положение кончика гребня на седло под тенью к вечеру"


def attach_rest_crest_saddle(character_cls) -> None:
    """Тихо класть кончик гребня на седло под тенью к вечеру после пера."""
    character_cls.rest_crest_saddle = rest_crest_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        crest_triggers = (
            "положи гребень",
            "положи гребень на седло",
            "положение гребня на седло",
            "рест крест седло",
            "положи после пера гребень",
        )
        if any(word in msg for word in crest_triggers):
            return self.rest_crest_saddle(_crest_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
