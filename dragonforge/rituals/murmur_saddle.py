"""В воскресенье 11 октября к вечеру после тихого опирания подбородком в седле: тихо бормочет в седле под тенью крыла, седло не снимаем.

Запуск: см. examples/sunday_evening_murmur_saddle.py
"""

from datetime import datetime


def murmur_saddle(self, place: str = "тихое бормотание в седле под тенью к вечеру") -> str:
    """После опирания подбородком: тихо бормочет в седле, седло не снимая."""
    self.soul.strengthen_habit("тихо бормочет в седле под тенью к вечеру", amount=0.05)
    self.soul.strengthen_habit("тихо опирается подбородком в седле под тенью к вечеру", amount=0.01)
    strength = self.soul.habits.get("тихо бормочет в седле под тенью к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое бормотание в седле под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо бормочет в седле под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "murmur_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.58,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо бормочет что-то мягкое, опираясь подбородком в седле под тенью крыла, седло на месте*  \n"
        f"После опирания подбородком хорошо тихо бормотать, всадник. Это — {note}. "
        f"Слова почти неслышные, тёплые, как дыхание. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо бормотать в седле под тенью к вечеру: {strength:.0%}. Можно помечтать о спокойном сне вместе."
    )


def _murmur_place(message: str) -> str:
    msg = message.lower()
    if "бормоч" in msg or "мурмур" in msg:
        return "тихое бормотание в седле"
    if "седл" in msg:
        return "бормотание в седле под тенью"
    return "тихое бормотание в седле под тенью к вечеру"


def attach_murmur_saddle(character_cls) -> None:
    """Тихо бормотать в седле под тенью к вечеру."""
    character_cls.murmur_saddle = murmur_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        murmur_triggers = (
            "бормочи в седле",
            "побормочи в седле",
            "мурмур седло",
            "тихо бормочи",
            "бормочи после подбородка",
        )
        if any(word in msg for word in murmur_triggers):
            return self.murmur_saddle(_murmur_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
