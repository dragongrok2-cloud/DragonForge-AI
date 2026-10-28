"""В воскресенье 11 октября к вечеру после тихой улыбки в седле: тихо опирается подбородком в седле под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_rest_chin_saddle.py
"""

from datetime import datetime


def rest_chin_saddle(self, place: str = "тихое опирание подбородком в седле под тенью к вечеру") -> str:
    """После улыбки: тихо опирается подбородком в седле, седло не снимая."""
    self.soul.strengthen_habit("тихо опирается подбородком в седле под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо улыбается в седле под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо опирается подбородком в седле под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое опирание подбородком в седле под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо опирается подбородком в седле под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_chin_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.59,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо опирается подбородком о луку или ближе к всаднику в седле под тенью крыла, седло на месте*  \n"
        f"После улыбки хорошо опереться подбородком, всадник. Это — {note}. "
        f"Подбородок мягко лежит, дыхание ровное, прохлада крыла успокаивает. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо опираться подбородком в седле под тенью к вечеру: {strength:.0%}. Можно помечтать о завтрашнем полёте вместе."
    )


def _rest_chin_place(message: str) -> str:
    msg = message.lower()
    if "подбород" in msg:
        return "тихое опирание подбородком в седле"
    if "седл" in msg:
        return "опирание подбородком в седле под тенью"
    return "тихое опирание подбородком в седле под тенью к вечеру"


def attach_rest_chin_saddle(character_cls) -> None:
    """Тихо опираться подбородком в седле под тенью к вечеру."""
    character_cls.rest_chin_saddle = rest_chin_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        rest_triggers = (
            "опрись подбородком",
            "опирись подбородком",
            "подбородок в седле",
            "рест чин седло",
            "опрись после улыбки",
        )
        if any(word in msg for word in rest_triggers):
            return self.rest_chin_saddle(_rest_chin_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
