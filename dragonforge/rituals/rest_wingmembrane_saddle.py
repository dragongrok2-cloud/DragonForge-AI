"""К вечеру после тихого положения сустава крыла: тихо положить мембрану крыла на седло под тенью, седло не снимаем.

Запуск: см. examples/monday_evening_rest_wingmembrane_saddle.py
"""

from datetime import datetime


def rest_wingmembrane_saddle(self, place: str = "тихое положение мембраны крыла на седло под тенью к вечеру") -> str:
    """После сустава: тихо кладёт мембрану крыла на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт мембрану крыла на седло под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт сустав крыла на седло под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт мембрану крыла на седло под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение мембраны крыла на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт мембрану крыла на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_wingmembrane_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт мембрану крыла на седло под тенью, седло на месте*  \n"
        f"После сустава хорошо положить мембрану, всадник. Это — {note}. "
        f"Тёплая мембрана крыла лежит на коже седла, дыхание глубокое и ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть мембрану крыла на седло под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _wingmembrane_place(message: str) -> str:
    msg = message.lower()
    if "мембран" in msg or "membrane" in msg:
        return "тихое положение мембраны крыла на седло"
    if "положи" in msg or "седл" in msg:
        return "положение мембраны крыла на седло под тенью"
    return "тихое положение мембраны крыла на седло под тенью к вечеру"


def attach_rest_wingmembrane_saddle(character_cls) -> None:
    """Тихо класть мембрану крыла на седло под тенью к вечеру."""
    character_cls.rest_wingmembrane_saddle = rest_wingmembrane_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        wingmembrane_triggers = (
            "положи мембрану крыла",
            "положи мембрану крыла на седло",
            "мембрана крыла на седло",
            "рест вингмембран седло",
            "положи после сустава",
        )
        if any(word in msg for word in wingmembrane_triggers):
            return self.rest_wingmembrane_saddle(_wingmembrane_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
