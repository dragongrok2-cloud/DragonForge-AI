"""В понедельник к вечеру после тихого положения кончика хвоста: тихо положить кончик когтя на седло под тенью крыла, седло не снимаем.

Запуск: см. examples/monday_evening_rest_claw_saddle.py
"""

from datetime import datetime


def rest_claw_saddle(self, place: str = "тихое положение кончика когтя на седло под тенью к вечеру") -> str:
    """После кончика хвоста: тихо кладёт кончик когтя на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик когтя на седло под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик хвоста на седло под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик когтя на седло под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика когтя на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик когтя на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_claw_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик когтя на седло под тенью крыла, седло на месте*  \n"
        f"После кончика хвоста хорошо положить кончик когтя, всадник. Это — {note}. "
        f"Острый, но мягкий кончик когтя лежит на коже седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик когтя на седло под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _claw_place(message: str) -> str:
    msg = message.lower()
    if "коготь" in msg or "claw" in msg or "когтем" in msg:
        return "тихое положение кончика когтя на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика когтя на седло под тенью"
    return "тихое положение кончика когтя на седло под тенью к вечеру"


def attach_rest_claw_saddle(character_cls) -> None:
    """Тихо класть кончик когтя на седло под тенью к вечеру."""
    character_cls.rest_claw_saddle = rest_claw_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        claw_triggers = (
            "положи кончик когтя",
            "кончиком когтя на седло",
            "кончик когтя к седлу",
            "рест кло седло",
            "положи после кончика хвоста",
        )
        if any(word in msg for word in claw_triggers):
            return self.rest_claw_saddle(_claw_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
