"""К вечеру после морды: тихо положить кончик носа на седло под тенью, седло не снимаем.

Запуск: см. examples/wednesday_evening_rest_nose_saddle.py
"""

from datetime import datetime


def rest_nose_saddle(self, place: str = "тихое положение кончика носа на седло под тенью к вечеру") -> str:
    """После морды: тихо кладёт кончик носа на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик носа на седло под тенью к вечеру после морды", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик морды на седло под тенью к вечеру после горла", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик носа на седло под тенью к вечеру после морды", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика носа на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик носа на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_nose_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик носа на седло под тенью, седло на месте*  \n"
        f"После морды хорошо положить кончик носа, всадник. Это — {note}. "
        f"Тёплый нос уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик носа на седло под тенью к вечеру после морды: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _nose_place(message: str) -> str:
    msg = message.lower()
    if "нос" in msg or "nose" in msg or "кончик" in msg:
        return "тихое положение кончика носа на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика носа на седло под тенью"
    return "тихое положение кончика носа на седло под тенью к вечеру"


def attach_rest_nose_saddle(character_cls) -> None:
    """Тихо класть кончик носа на седло под тенью к вечеру после морды."""
    character_cls.rest_nose_saddle = rest_nose_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        nose_triggers = (
            "положи нос",
            "положи нос на седло",
            "положение носа на седло",
            "рест нос седло",
            "положи после морды нос",
        )
        if any(word in msg for word in nose_triggers):
            return self.rest_nose_saddle(_nose_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
