"""Утренние ритуалы, которые крепятся на персонаже."""

from datetime import datetime


def blot_scale(self, place: str = "роса с чешуйки после ладони") -> str:
    """После подъёма ладони: промокнуть росу с чешуйки, не снимая седла."""
    self.soul.strengthen_habit("промокает чешуйку после ладони", amount=0.05)
    self.soul.strengthen_habit("поднимает ладонь после нажатия", amount=0.01)
    strength = self.soul.habits.get("промокает чешуйку после ладони", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "роса с чешуйки после ладони"
    self.memory.remember(
        f"{self.name} промокнул росу с чешуйки после ладони: {note}, привычка {strength:.0%}",
        metadata={"type": "blot_scale", "timestamp": str(datetime.now()), "place": note},
        importance=0.55,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    energy_after = self.soul.emotional_state["energy"]
    return (
        f"*краем крыла промокает росу с чешуйки у луки, ладонь уже поднята*  \n"
        f"Ладонь ушла, а капля осталась, всадник. Это — {note}. "
        f"Чешуйка сухая, перчатка не липнет, край не поднимает ветер. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}, энергия {energy_after:.2f}. "
        f"Привычка промокать чешуйку: {strength:.0%}. Можно держать седло и встречать утро."
    )


def _blot_note(message: str) -> str:
    msg = message.lower()
    if "гнезд" in msg:
        return "роса с чешуйки у гнезда"
    if "стрем" in msg:
        return "роса с чешуйки у стремени"
    if "лук" in msg:
        return "роса с чешуйки у луки"
    return "роса с чешуйки после ладони"


def attach(character_cls) -> None:
    """Повесить промокание росы на персонажа и на разговор."""
    character_cls.blot_scale = blot_scale
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        triggers = (
            "промокни чешуй",
            "роса с чешуй",
            "промокнуть край",
            "роса после ладони",
            "промокни край чешуй",
        )
        if any(word in msg for word in triggers):
            return self.blot_scale(_blot_note(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
