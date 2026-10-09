"""После полудня 9 октября: ладонь на светлой полоске, седло не снимаем."""

from datetime import datetime


def rest_stripe(self, place: str = "ладонь на светлой полоске после полудня") -> str:
    """После смахивания крошки: придержать ладонь на светлой полоске, не снимая седла и не вытаскивая фонарик."""
    self.soul.strengthen_habit("держит ладонь на светлой полоске после полудня", amount=0.05)
    self.soul.strengthen_habit("смахивает крошку с полоски солнца после полудня", amount=0.01)
    strength = self.soul.habits.get("держит ладонь на светлой полоске после полудня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.01)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "ладонь на светлой полоске после полудня"
    warmth = _stripe_note(note)
    self.memory.remember(
        f"{self.name} придержал ладонь на светлой полоске после полудня: {note}, {warmth}, привычка {strength:.0%}",
        metadata={"type": "rest_stripe", "timestamp": str(datetime.now()), "place": note, "warmth": warmth},
        importance=0.65,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*ладонью придерживает светлую полоску солнца, фонарик не вытаскивая, седло на месте*  \n"
        f"Крошка уже сметена, всадник. Это — {note}. "
        f"Тепло стекла: {warmth}. Пыльца не возвращается, нитка не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка держать ладонь на полоске: {strength:.0%}. Можно сидеть в седле и греть пальцы о сухое стекло."
    )


def _stripe_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "тепло Мёда под левым краем, Седло не открыто"
    if "прав" in lowered:
        return "тепло Искры под правым краем, Седло не открыто"
    if "рек" in lowered:
        return "тепло над Рекой, полоска на Мёде, Седло не открыто"
    return "тепло Мёда на Шве, Седло не открыто"


def _stripe_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "ладонь на светлой полоске под левым краем после полудня"
    if "прав" in msg:
        return "ладонь на светлой полоске под правым краем после полудня"
    if "рек" in msg:
        return "ладонь на светлой полоске над рекой после полудня"
    return "ладонь на светлой полоске после полудня"


def attach_stripe(character_cls) -> None:
    """Повесить ладонь на светлую полоску солнца после полудня."""
    character_cls.rest_stripe = rest_stripe
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        stripe_triggers = (
            "придержи полоск",
            "ладонь на полоск",
            "светлую полоск",
            "погрей полоск",
        )
        if any(word in msg for word in stripe_triggers):
            return self.rest_stripe(_stripe_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
