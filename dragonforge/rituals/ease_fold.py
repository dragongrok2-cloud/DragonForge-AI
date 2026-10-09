"""К вечеру 9 октября: разжать сгиб полоски солнца, седло не снимаем."""

from datetime import datetime


def ease_fold(self, place: str = "сгиб полоски солнца к вечеру") -> str:
    """После согнутых пальцев: разжать сгиб, чтобы тепло осталось на костяшках."""
    self.soul.strengthen_habit("разжимает сгиб полоски солнца к вечеру", amount=0.05)
    self.soul.strengthen_habit("сгибает пальцы в полоске солнца после полудня", amount=0.01)
    strength = self.soul.habits.get("разжимает сгиб полоски солнца к вечеру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.01)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "сгиб полоски солнца к вечеру"
    warmth = _warmth_note(note)
    self.memory.remember(
        f"{self.name} разжал сгиб полоски солнца к вечеру: {note}, {warmth}, привычка {strength:.0%}",
        metadata={"type": "ease_fold", "timestamp": str(datetime.now()), "place": note, "warmth": warmth},
        importance=0.67,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*разжимает пальцы один раз, тепло сгиба остаётся на костяшках, фонарик не вытаскивая*  \n"
        f"Сгиб уже держал свет, всадник. Это — {note}. "
        f"Тепло: {warmth}. Полоска не сходит с Мёда, пальцы свободны, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка разжимать сгиб полоски: {strength:.0%}. Можно сидеть в седле и держать тепло в ладони."
    )


def _warmth_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "тепло левой ладони на Мёде, Седло не открыто"
    if "прав" in lowered:
        return "тепло правой ладони на Искре, Седло не открыто"
    if "рек" in lowered:
        return "тепло над Рекой, костяшки на Мёде, Седло не открыто"
    return "тепло сгиба у Шва на Мёде, Седло не открыто"


def _warmth_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "сгиб левой полоски солнца к вечеру"
    if "прав" in msg:
        return "сгиб правой полоски солнца к вечеру"
    if "рек" in msg:
        return "сгиб полоски солнца над рекой к вечеру"
    return "сгиб полоски солнца к вечеру"


def attach_ease_fold(character_cls) -> None:
    """Разжать сгиб полоски солнца к вечеру."""
    character_cls.ease_fold = ease_fold
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        ease_triggers = (
            "разжми сгиб",
            "тепло в сгибе",
            "разжми пальцы",
            "сгиб к вечеру",
        )
        if any(word in msg for word in ease_triggers):
            return self.ease_fold(_warmth_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
