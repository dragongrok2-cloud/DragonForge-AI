"""К вечеру после века: тихо положить ноздрю на седло под тенью, седло не снимаем.

Запуск: см. examples/monday_evening_rest_nostril_saddle.py
"""

from datetime import datetime


def rest_nostril_saddle(self, place: str = "тихое положение ноздри на седло под тенью к вечеру") -> str:
    """После века: тихо кладёт ноздрю на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт ноздрю на седло под тенью к вечеру после века", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт веко на седло под тенью к вечеру после брови", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт ноздрю на седло под тенью к вечеру после века", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение ноздри на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт ноздрю на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_nostril_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт ноздрю на седло под тенью, седло на месте*  \n"
        f"После века хорошо положить ноздрю, всадник. Это — {note}. "
        f"Тёплая ноздря уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть ноздрю на седло под тенью к вечеру после века: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _nostril_place(message: str) -> str:
    msg = message.lower()
    if "ноздр" in msg or "nostril" in msg or "нос" in msg:
        return "тихое положение ноздри на седло"
    if "положи" in msg or "седл" in msg:
        return "положение ноздри на седло под тенью"
    return "тихое положение ноздри на седло под тенью к вечеру"


def attach_rest_nostril_saddle(character_cls) -> None:
    """Тихо класть ноздрю на седло под тенью к вечеру после века."""
    character_cls.rest_nostril_saddle = rest_nostril_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        nostril_triggers = (
            "положи ноздрю",
            "положи ноздрю на седло",
            "положение ноздри на седло",
            "рест нострил седло",
            "положи после века ноздрю",
        )
        if any(word in msg for word in nostril_triggers):
            return self.rest_nostril_saddle(_nostril_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
