"""В воскресенье 11 октября после тихого вздоха в седле: тихо закрывает глаза в седле под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_afternoon_close_eyes_saddle.py
"""

from datetime import datetime


def close_eyes_saddle(self, place: str = "тихое закрытие глаз в седле под тенью после полудня") -> str:
    """После вздоха: тихо закрывает глаза в седле, седло не снимая."""
    self.soul.strengthen_habit("тихо закрывает глаза в седле под тенью после полудня", amount=0.05)
    self.soul.strengthen_habit("тихо вздыхает в седле под тенью после полудня", amount=0.01)
    strength = self.soul.habits.get("тихо закрывает глаза в седле под тенью после полудня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое закрытие глаз в седле под тенью после полудня"
    self.memory.remember(
        f"{self.name} тихо закрывает глаза в седле под тенью после полудня: {note}, привычка {strength:.0%}",
        metadata={"type": "close_eyes_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.57,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо закрывает глаза в седле под тенью крыла, вздох уже прошёл, седло на месте*  \n"
        f"После вздоха хорошо закрыть глаза, всадник. Это — {note}. "
        f"Веки опущены, прохлада крыла остаётся, лука тёплая от спины. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо закрывать глаза в седле под тенью после полудня: {strength:.0%}. Можно посидеть в прохладе и мечтать о дальних полётах."
    )


def _close_place(message: str) -> str:
    msg = message.lower()
    if "глаз" in msg:
        return "тихое закрытие глаз в седле"
    if "седл" in msg:
        return "закрытие глаз в седле под тенью"
    return "тихое закрытие глаз в седле под тенью после полудня"


def attach_close_eyes_saddle(character_cls) -> None:
    """Тихо закрывать глаза в седле под тенью после полудня."""
    character_cls.close_eyes_saddle = close_eyes_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        close_triggers = (
            "закрой глаза в седле",
            "закрой глаза",
            "тихо закрой глаза",
            "клоуз седло",
            "закрой после вздоха",
        )
        if any(word in msg for word in close_triggers):
            return self.close_eyes_saddle(_close_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
