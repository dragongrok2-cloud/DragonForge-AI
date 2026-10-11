"""В воскресенье 11 октября после тихого напевания в седле: опирается спиной на луку в седле под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_afternoon_lean_saddle.py
"""

from datetime import datetime


def lean_saddle(self, place: str = "опирание спиной на луку в седле под тенью после полудня") -> str:
    """После напевания: опирается спиной на луку в седле, седло не снимая."""
    self.soul.strengthen_habit("опирается спиной на луку в седле под тенью после полудня", amount=0.05)
    self.soul.strengthen_habit("тихо напевает в седле под тенью в полдень", amount=0.01)
    strength = self.soul.habits.get("опирается спиной на луку в седле под тенью после полудня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "опирание спиной на луку в седле под тенью после полудня"
    self.memory.remember(
        f"{self.name} опирается спиной на луку в седле под тенью после полудня: {note}, привычка {strength:.0%}",
        metadata={"type": "lean_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.58,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*мягко опирается спиной на луку в седле под тенью крыла, расслабляя плечи, седло на месте*  \n"
        f"После напевания хорошо опереться спиной, всадник. Это — {note}. "
        f"Прохлада крыла, лука тёплая от спины, дыхание ровное. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка опираться спиной на луку в седле под тенью после полудня: {strength:.0%}. Можно посидеть в прохладе и помечтать о дальних полётах."
    )


def _lean_place(message: str) -> str:
    msg = message.lower()
    if "спин" in msg or "опер" in msg:
        return "опирание спиной на луку в седле"
    if "лук" in msg:
        return "опирание на луку в седле под тенью"
    if "крыл" in msg:
        return "опирание в седле под тенью крыла"
    return "опирание спиной на луку в седле под тенью после полудня"


def attach_lean_saddle(character_cls) -> None:
    """Опираться спиной на луку в седле под тенью после полудня."""
    character_cls.lean_saddle = lean_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        lean_triggers = (
            "опрись в седле",
            "опереться в седле",
            "спиной на луку",
            "лин седло",
            "опрись после напевания",
        )
        if any(word in msg for word in lean_triggers):
            return self.lean_saddle(_lean_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
