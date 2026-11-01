"""К вечеру после тихого положения крыла: тихо положить основание крыла на седло под тенью, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_wingbase_saddle.py
"""

from datetime import datetime


def rest_wingbase_saddle(self, place: str = "тихое положение основания крыла на седло под тенью к вечеру") -> str:
    """После крыла: тихо кладёт основание крыла на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт основание крыла на седло под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт крыло на седло под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт основание крыла на седло под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение основания крыла на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт основание крыла на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_wingbase_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт основание крыла на седло под тенью, седло на месте*  \n"
        f"После крыла хорошо положить основание, всадник. Это — {note}. "
        f"Тёплое основание крыла лежит на коже седла, дыхание глубокое и ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть основание крыла на седло под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _wingbase_place(message: str) -> str:
    msg = message.lower()
    if "основан" in msg or "base" in msg:
        return "тихое положение основания крыла на седло"
    if "положи" in msg or "седл" in msg:
        return "положение основания крыла на седло под тенью"
    return "тихое положение основания крыла на седло под тенью к вечеру"


def attach_rest_wingbase_saddle(character_cls) -> None:
    """Тихо класть основание крыла на седло под тенью к вечеру."""
    character_cls.rest_wingbase_saddle = rest_wingbase_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        wingbase_triggers = (
            "положи основание крыла",
            "положи основание крыла на седло",
            "основание крыла на седло",
            "рест вингбейс седло",
            "положи после крыла",
        )
        if any(word in msg for word in wingbase_triggers):
            return self.rest_wingbase_saddle(_wingbase_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
