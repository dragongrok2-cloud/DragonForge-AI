"""К вечеру после горла: тихо положить кончик морды на седло под тенью, седло не снимаем.

Запуск: см. examples/tuesday_evening_rest_muzzle_saddle.py
"""

from datetime import datetime


def rest_muzzle_saddle(self, place: str = "тихое положение кончика морды на седло под тенью к вечеру") -> str:
    """После горла: тихо кладёт кончик морды на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик морды на седло под тенью к вечеру после горла", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик горла на седло под тенью к вечеру после ваттла", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик морды на седло под тенью к вечеру после горла", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика морды на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик морды на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_muzzle_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик морды на седло под тенью, седло на месте*  \n"
        f"После горла хорошо положить кончик морды, всадник. Это — {note}. "
        f"Тёплая морда уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик морды на седло под тенью к вечеру после горла: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _muzzle_place(message: str) -> str:
    msg = message.lower()
    if "морд" in msg or "muzzle" in msg or "кончик" in msg:
        return "тихое положение кончика морды на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика морды на седло под тенью"
    return "тихое положение кончика морды на седло под тенью к вечеру"


def attach_rest_muzzle_saddle(character_cls) -> None:
    """Тихо класть кончик морды на седло под тенью к вечеру после горла."""
    character_cls.rest_muzzle_saddle = rest_muzzle_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        muzzle_triggers = (
            "положи морду",
            "положи морду на седло",
            "положение морды на седло",
            "рест мазл седло",
            "положи после горла морду",
        )
        if any(word in msg for word in muzzle_triggers):
            return self.rest_muzzle_saddle(_muzzle_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
