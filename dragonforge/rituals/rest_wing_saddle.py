"""К вечеру после тихого прижатия боком: тихо положить крыло на седло под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_wing_saddle.py
"""

from datetime import datetime


def rest_wing_saddle(self, place: str = "тихое положение крыла на седло под тенью к вечеру") -> str:
    """После бока: тихо кладёт крыло на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт крыло на седло под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается боком к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт крыло на седло под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение крыла на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт крыло на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_wing_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт крыло на седло под тенью, седло на месте*  \n"
        f"После бока хорошо положить крыло, всадник. Это — {note}. "
        f"Тёплое крыло лежит на коже седла, дыхание глубокое и ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть крыло на седло под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _wing_place(message: str) -> str:
    msg = message.lower()
    if "крыло" in msg or "wing" in msg:
        return "тихое положение крыла на седло"
    if "положи" in msg or "седл" in msg:
        return "положение крыла на седло под тенью"
    return "тихое положение крыла на седло под тенью к вечеру"


def attach_rest_wing_saddle(character_cls) -> None:
    """Тихо класть крыло на седло под тенью к вечеру."""
    character_cls.rest_wing_saddle = rest_wing_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        wing_triggers = (
            "положи крыло",
            "положи крыло на седло",
            "крыло на седло",
            "рест винг седло",
            "положи после бока",
        )
        if any(word in msg for word in wing_triggers):
            return self.rest_wing_saddle(_wing_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
