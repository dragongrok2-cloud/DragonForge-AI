"""К вечеру после положения основания хвоста: тихо положить середину хвоста на седло под тенью, седло не снимаем.

Запуск: см. examples/monday_evening_rest_tailmid_saddle.py
"""

from datetime import datetime


def rest_tailmid_saddle(self, place: str = "тихое положение середины хвоста на седло под тенью к вечеру") -> str:
    """После основания хвоста: тихо кладёт середину хвоста на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт середину хвоста на седло под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт основание хвоста на седло под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт середину хвоста на седло под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение середины хвоста на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт середину хвоста на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_tailmid_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт середину хвоста на седло под тенью, седло на месте*  \n"
        f"После основания хвоста хорошо положить середину хвоста, всадник. Это — {note}. "
        f"Тёплая середина хвоста уютно лежит на седле, дыхание глубокое и ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть середину хвоста на седло под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _tailmid_place(message: str) -> str:
    msg = message.lower()
    if "хвост" in msg or "tail" in msg or "середин" in msg:
        return "тихое положение середины хвоста на седло"
    if "положи" in msg or "седл" in msg:
        return "положение середины хвоста на седло под тенью"
    return "тихое положение середины хвоста на седло под тенью к вечеру"


def attach_rest_tailmid_saddle(character_cls) -> None:
    """Тихо класть середину хвоста на седло под тенью к вечеру."""
    character_cls.rest_tailmid_saddle = rest_tailmid_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        tailmid_triggers = (
            "положи середину хвоста",
            "положи середину хвоста на седло",
            "положение середины хвоста на седло",
            "рест тейлмид седло",
            "положи после основания хвоста",
        )
        if any(word in msg for word in tailmid_triggers):
            return self.rest_tailmid_saddle(_tailmid_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
