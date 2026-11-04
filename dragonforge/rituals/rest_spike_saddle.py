"""К вечеру после гребня: тихо положить кончик шипа на седло под тенью, седло не снимаем.

Запуск: см. examples/tuesday_evening_rest_spike_saddle.py
"""

from datetime import datetime


def rest_spike_saddle(self, place: str = "тихое положение кончика шипа на седло под тенью к вечеру") -> str:
    """После гребня: тихо кладёт кончик шипа на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик шипа на седло под тенью к вечеру после гребня", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик гребня на седло под тенью к вечеру после пера", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик шипа на седло под тенью к вечеру после гребня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика шипа на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик шипа на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_spike_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик шипа на седло под тенью, седло на месте*  \n"
        f"После гребня хорошо положить кончик шипа, всадник. Это — {note}. "
        f"Тёплый шип уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик шипа на седло под тенью к вечеру после гребня: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _spike_place(message: str) -> str:
    msg = message.lower()
    if "шип" in msg or "spike" in msg or "кончик" in msg:
        return "тихое положение кончика шипа на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика шипа на седло под тенью"
    return "тихое положение кончика шипа на седло под тенью к вечеру"


def attach_rest_spike_saddle(character_cls) -> None:
    """Тихо класть кончик шипа на седло под тенью к вечеру после гребня."""
    character_cls.rest_spike_saddle = rest_spike_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        spike_triggers = (
            "положи шип",
            "положи шип на седло",
            "положение шипа на седло",
            "рест спайк седло",
            "положи после гребня шип",
        )
        if any(word in msg for word in spike_triggers):
            return self.rest_spike_saddle(_spike_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
