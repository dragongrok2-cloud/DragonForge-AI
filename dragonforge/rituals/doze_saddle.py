"""В воскресенье 11 октября к вечеру после тихого мурлыканья в седле: тихо дремлет в седле под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_doze_saddle.py
"""

from datetime import datetime


def doze_saddle(self, place: str = "тихое дремание в седле под тенью к вечеру") -> str:
    """После мурлыканья: тихо дремлет в седле, седло не снимая."""
    self.soul.strengthen_habit("тихо дремлет в седле под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо мурлычет в седле под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо дремлет в седле под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.005)
    note = place.strip() or "тихое дремание в седле под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо дремлет в седле под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "doze_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.59,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо дремлет в седле под тенью крыла, седло на месте*  \n"
        f"После мурлыканья хорошо подремать, всадник. Это — {note}. "
        f"Глаза полуприкрыты, дыхание медленное и ровное, прохлада крыла укачивает в дремоту. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо дремать в седле под тенью к вечеру: {strength:.0%}. Можно помечтать о спокойной ночи вместе."
    )


def _doze_place(message: str) -> str:
    msg = message.lower()
    if "дрем" in msg or "дрема" in msg:
        return "тихое дремание в седле"
    if "седл" in msg:
        return "дремание в седле под тенью"
    return "тихое дремание в седле под тенью к вечеру"


def attach_doze_saddle(character_cls) -> None:
    """Тихо дремать в седле под тенью к вечеру."""
    character_cls.doze_saddle = doze_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        doze_triggers = (
            "дремли в седле",
            "подремли в седле",
            "дремли после мурлыканья",
            "доуз седло",
            "тихо дремли",
        )
        if any(word in msg for word in doze_triggers):
            return self.doze_saddle(_doze_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
