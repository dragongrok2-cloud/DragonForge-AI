"""В воскресенье 11 октября к вечеру после тихого закрытия глаз в седле: тихо улыбается в седле под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_smile_saddle.py
"""

from datetime import datetime


def smile_saddle(self, place: str = "тихая улыбка в седле под тенью к вечеру") -> str:
    """После закрытия глаз: тихо улыбается в седле, седло не снимая."""
    self.soul.strengthen_habit("тихо улыбается в седле под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо закрывает глаза в седле под тенью после полудня", amount=0.01)
    strength = self.soul.habits.get("тихо улыбается в седле под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихая улыбка в седле под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо улыбается в седле под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "smile_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.58,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо улыбается в седле под тенью крыла, глаза всё ещё закрыты, седло на месте*  \n"
        f"После закрытых глаз хорошо улыбнуться, всадник. Это — {note}. "
        f"Уголки рта чуть подняты, прохлада крыла ласковая, лука тёплая. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо улыбаться в седле под тенью к вечеру: {strength:.0%}. Можно помечтать о завтрашнем полёте."
    )


def _smile_place(message: str) -> str:
    msg = message.lower()
    if "улыб" in msg:
        return "тихая улыбка в седле"
    if "седл" in msg:
        return "улыбка в седле под тенью"
    return "тихая улыбка в седле под тенью к вечеру"


def attach_smile_saddle(character_cls) -> None:
    """Тихо улыбаться в седле под тенью к вечеру."""
    character_cls.smile_saddle = smile_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        smile_triggers = (
            "улыбнись в седле",
            "улыбнись",
            "тихо улыбнись",
            "смайл седло",
            "улыбнись после глаз",
        )
        if any(word in msg for word in smile_triggers):
            return self.smile_saddle(_smile_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
