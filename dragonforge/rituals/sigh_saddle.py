"""В воскресенье 11 октября после опирания спиной на луку в седле: тихо вздыхает в седле под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_afternoon_sigh_saddle.py
"""

from datetime import datetime


def sigh_saddle(self, place: str = "тихий вздох в седле под тенью после полудня") -> str:
    """После опирания: тихо вздыхает в седле, седло не снимая."""
    self.soul.strengthen_habit("тихо вздыхает в седле под тенью после полудня", amount=0.05)
    self.soul.strengthen_habit("опирается спиной на луку в седле под тенью после полудня", amount=0.01)
    strength = self.soul.habits.get("тихо вздыхает в седле под тенью после полудня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихий вздох в седле под тенью после полудня"
    self.memory.remember(
        f"{self.name} тихо вздыхает в седле под тенью после полудня: {note}, привычка {strength:.0%}",
        metadata={"type": "sigh_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.57,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо вздыхает в седле под тенью крыла, спина уже на луке, седло на месте*  \n"
        f"После опирания хорошо вздохнуть, всадник. Это — {note}. "
        f"Дыхание мягкое, прохлада крыла остаётся, лука тёплая от спины. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо вздыхать в седле под тенью после полудня: {strength:.0%}. Можно посидеть в прохладе и мечтать о дальних полётах."
    )


def _sigh_place(message: str) -> str:
    msg = message.lower()
    if "вздох" in msg:
        return "тихий вздох в седле"
    if "седл" in msg:
        return "вздох в седле под тенью"
    return "тихий вздох в седле под тенью после полудня"


def attach_sigh_saddle(character_cls) -> None:
    """Тихо вздыхать в седле под тенью после полудня."""
    character_cls.sigh_saddle = sigh_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        sigh_triggers = (
            "вздохни в седле",
            "вздох в седле",
            "тихо вздохни",
            "сай седло",
            "вздохни после опирания",
        )
        if any(word in msg for word in sigh_triggers):
            return self.sigh_saddle(_sigh_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
