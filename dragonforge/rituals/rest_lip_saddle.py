"""К вечеру после ноздри: тихо положить губу на седло под тенью, седло не снимаем.

Запуск: см. examples/monday_evening_rest_lip_saddle.py
"""

from datetime import datetime


def rest_lip_saddle(self, place: str = "тихое положение губы на седло под тенью к вечеру") -> str:
    """После ноздри: тихо кладёт губу на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт губу на седло под тенью к вечеру после ноздри", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт ноздрю на седло под тенью к вечеру после века", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт губу на седло под тенью к вечеру после ноздри", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение губы на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт губу на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_lip_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт губу на седло под тенью, седло на месте*  \n"
        f"После ноздри хорошо положить губу, всадник. Это — {note}. "
        f"Тёплая губа уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть губу на седло под тенью к вечеру после ноздри: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _lip_place(message: str) -> str:
    msg = message.lower()
    if "губ" in msg or "lip" in msg or "уст" in msg:
        return "тихое положение губы на седло"
    if "положи" in msg or "седл" in msg:
        return "положение губы на седло под тенью"
    return "тихое положение губы на седло под тенью к вечеру"


def attach_rest_lip_saddle(character_cls) -> None:
    """Тихо класть губу на седло под тенью к вечеру после ноздри."""
    character_cls.rest_lip_saddle = rest_lip_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        lip_triggers = (
            "положи губу",
            "положи губу на седло",
            "положение губы на седло",
            "рест лип седло",
            "положи после ноздри губу",
        )
        if any(word in msg for word in lip_triggers):
            return self.rest_lip_saddle(_lip_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
