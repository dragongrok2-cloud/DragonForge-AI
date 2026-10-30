"""В понедельник к вечеру после тихого положения кончика крыла: тихо положить кончик хвоста на седло под тенью крыла, седло не снимаем.

Запуск: см. examples/monday_evening_rest_tail_saddle.py
"""

from datetime import datetime


def rest_tail_saddle(self, place: str = "тихое положение кончика хвоста на седло под тенью к вечеру") -> str:
    """После кончика крыла: тихо кладёт кончик хвоста на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик хвоста на седло под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик крыла на седло под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик хвоста на седло под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика хвоста на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик хвоста на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_tail_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик хвоста на седло под тенью крыла, седло на месте*  \n"
        f"После кончика крыла хорошо положить кончик хвоста, всадник. Это — {note}. "
        f"Мягкий кончик хвоста лежит на коже седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик хвоста на седло под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _tail_place(message: str) -> str:
    msg = message.lower()
    if "хвост" in msg or "tail" in msg or "хвостом" in msg:
        return "тихое положение кончика хвоста на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика хвоста на седло под тенью"
    return "тихое положение кончика хвоста на седло под тенью к вечеру"


def attach_rest_tail_saddle(character_cls) -> None:
    """Тихо класть кончик хвоста на седло под тенью к вечеру."""
    character_cls.rest_tail_saddle = rest_tail_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        tail_triggers = (
            "положи кончик хвоста",
            "кончиком хвоста на седло",
            "кончик хвоста к седлу",
            "рест тейл седло",
            "положи после кончика крыла",
        )
        if any(word in msg for word in tail_triggers):
            return self.rest_tail_saddle(_tail_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
