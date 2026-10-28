"""В воскресенье 11 октября к вечеру после тихого бормотания в седле: тихо зевает в седле под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_yawn_saddle.py
"""

from datetime import datetime


def yawn_saddle(self, place: str = "тихое зевание в седле под тенью к вечеру") -> str:
    """После бормотания: тихо зевает в седле, седло не снимая."""
    self.soul.strengthen_habit("тихо зевает в седле под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо бормочет в седле под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо зевает в седле под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое зевание в седле под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо зевает в седле под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "yawn_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.57,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо зевает, опираясь подбородком в седле под тенью крыла, седло на месте*  \n"
        f"После бормотания хорошо тихо позевать, всадник. Это — {note}. "
        f"Рот широко открывается, глаза прикрываются, тёплый выдох. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо зевать в седле под тенью к вечеру: {strength:.0%}. Можно помечтать о спокойном сне вместе."
    )


def _yawn_place(message: str) -> str:
    msg = message.lower()
    if "зев" in msg or "йоун" in msg:
        return "тихое зевание в седле"
    if "седл" in msg:
        return "зевание в седле под тенью"
    return "тихое зевание в седле под тенью к вечеру"


def attach_yawn_saddle(character_cls) -> None:
    """Тихо зевать в седле под тенью к вечеру."""
    character_cls.yawn_saddle = yawn_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        yawn_triggers = (
            "зевай в седле",
            "позевай в седле",
            "йоун седло",
            "тихо зевай",
            "зевай после бормотания",
        )
        if any(word in msg for word in yawn_triggers):
            return self.yawn_saddle(_yawn_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
