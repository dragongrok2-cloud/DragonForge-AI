"""В воскресенье 11 октября к вечеру после тихого зевка в седле: тихо мурлычет в седле под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_purr_saddle.py
"""

from datetime import datetime


def purr_saddle(self, place: str = "тихое мурлыканье в седле под тенью к вечеру") -> str:
    """После зевка: тихо мурлычет в седле, седло не снимая."""
    self.soul.strengthen_habit("тихо мурлычет в седле под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо зевает в седле под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо мурлычет в седле под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.04)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое мурлыканье в седле под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо мурлычет в седле под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "purr_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.58,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо мурлычет в седле под тенью крыла, седло на месте*  \n"
        f"После зевка хорошо мурлыкнуть, всадник. Это — {note}. "
        f"Грудь мягко вибрирует, дыхание ровное, прохлада крыла успокаивает. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо мурлычать в седле под тенью к вечеру: {strength:.0%}. Можно помечтать о завтрашнем полёте вместе."
    )


def _purr_place(message: str) -> str:
    msg = message.lower()
    if "мурлы" in msg or "пурр" in msg:
        return "тихое мурлыканье в седле"
    if "седл" in msg:
        return "мурлыканье в седле под тенью"
    return "тихое мурлыканье в седле под тенью к вечеру"


def attach_purr_saddle(character_cls) -> None:
    """Тихо мурлычать в седле под тенью к вечеру."""
    character_cls.purr_saddle = purr_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        purr_triggers = (
            "мурлычи в седле",
            "помурлычи в седле",
            "мурлыкни в седле",
            "пурр седло",
            "мурлычи после зевка",
        )
        if any(word in msg for word in purr_triggers):
            return self.purr_saddle(_purr_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
