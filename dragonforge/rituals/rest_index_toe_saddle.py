"""К вечеру после тихого прижатия безымянного пальца стопы: тихо прижаться указательным пальцем стопы к седлу под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_index_toe_saddle.py
"""

from datetime import datetime


def rest_index_toe_saddle(self, place: str = "тихое прижатие указательного пальца стопы к седлу под тенью к вечеру") -> str:
    """После безымянного: тихо прижимается указательным пальцем стопы к седлу, седло не снимая."""
    self.soul.strengthen_habit("тихо прижимается указательным пальцем стопы к седлу под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо прижимается безымянным пальцем стопы к седлу под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо прижимается указательным пальцем стопы к седлу под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое прижатие указательного пальца стопы к седлу под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо прижимается указательным пальцем стопы к седлу под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_index_toe_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо прижимается указательным пальцем стопы к седлу под тенью крыла, седло на месте*  \n"
        f"После безымянного хорошо прижаться указательным пальцем стопы, всадник. Это — {note}. "
        f"Тёплый указательный палец лежит на коже седла, дыхание ровное, глаза полуприкрыты. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо прижиматься указательным пальцем стопы к седлу под тенью к вечеру: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _index_toe_place(message: str) -> str:
    msg = message.lower()
    if "указательн" in msg or "index" in msg or "указательным" in msg:
        return "тихое прижатие указательного пальца стопы к седлу"
    if "прижмись" in msg or "седл" in msg:
        return "прижатие указательного пальца стопы к седлу под тенью"
    return "тихое прижатие указательного пальца стопы к седлу под тенью к вечеру"


def attach_rest_index_toe_saddle(character_cls) -> None:
    """Тихо прижиматься указательным пальцем стопы к седлу под тенью к вечеру."""
    character_cls.rest_index_toe_saddle = rest_index_toe_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        index_toe_triggers = (
            "прижмись указательным пальцем",
            "прижмись к седлу указательным пальцем",
            "указательным пальцем к седлу",
            "рест индекс то седло",
            "прижмись после безымянного",
        )
        if any(word in msg for word in index_toe_triggers):
            return self.rest_index_toe_saddle(_index_toe_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
