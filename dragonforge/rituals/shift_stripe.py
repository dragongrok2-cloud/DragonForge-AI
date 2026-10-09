"""После полудня 9 октября: полоска солнца на костяшках, седло не снимаем."""

from datetime import datetime


def shift_stripe(self, place: str = "полоска солнца на костяшках после полудня") -> str:
    """После ладони на полоске: сдвинуть ладонь на чешуйку, чтобы свет лёг на костяшки."""
    self.soul.strengthen_habit("сдвигает полоску солнца на костяшки после полудня", amount=0.05)
    self.soul.strengthen_habit("держит ладонь на светлой полоске после полудня", amount=0.01)
    strength = self.soul.habits.get("сдвигает полоску солнца на костяшки после полудня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.01)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "полоска солнца на костяшках после полудня"
    warmth = _knuckle_note(note)
    self.memory.remember(
        f"{self.name} сдвинул полоску солнца на костяшки после полудня: {note}, {warmth}, привычка {strength:.0%}",
        metadata={"type": "shift_stripe", "timestamp": str(datetime.now()), "place": note, "warmth": warmth},
        importance=0.66,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*сдвигает ладонь на одну чешуйку, полоска солнца ложится на костяшки, фонарик не вытаскивая*  \n"
        f"Ладонь уже побыла на стекле, всадник. Это — {note}. "
        f"Тепло костяшек: {warmth}. Пальцы можно согнуть, пыльца не возвращается, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка сдвигать полоску на костяшки: {strength:.0%}. Можно сидеть в седле и шевелить пальцами в свете."
    )


def _knuckle_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "тепло Мёда на левых костяшках, Седло не открыто"
    if "прав" in lowered:
        return "тепло Искры на правых костяшках, Седло не открыто"
    if "рек" in lowered:
        return "тепло над Рекой, костяшки на Мёде, Седло не открыто"
    return "тепло Мёда на костяшках у Шва, Седло не открыто"


def _knuckle_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "полоска солнца на левых костяшках после полудня"
    if "прав" in msg:
        return "полоска солнца на правых костяшках после полудня"
    if "рек" in msg:
        return "полоска солнца на костяшках над рекой после полудня"
    return "полоска солнца на костяшках после полудня"


def attach_shift(character_cls) -> None:
    """Сдвинуть светлую полоску солнца на костяшки после полудня."""
    character_cls.shift_stripe = shift_stripe
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        shift_triggers = (
            "сдвинь полоск",
            "полоска на костяш",
            "костяшки на полоск",
            "сдвинь ладонь",
        )
        if any(word in msg for word in shift_triggers):
            return self.shift_stripe(_knuckle_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
