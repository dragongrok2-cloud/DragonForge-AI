"""Утренние и полуденные ритуалы, которые крепятся на персонаже."""

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


def fold_cloth(self, place: str = "край попоны под лукой после росы") -> str:
    """К полудню: сложить край попоны под луку, не снимая седла."""
    self.soul.strengthen_habit("складывает край попоны после росы", amount=0.05)
    self.soul.strengthen_habit("промокает чешуйку после ладони", amount=0.01)
    strength = self.soul.habits.get("складывает край попоны после росы", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "край попоны под лукой после росы"
    self.memory.remember(
        f"{self.name} сложил край попоны под луку после росы: {note}, привычка {strength:.0%}",
        metadata={"type": "fold_cloth", "timestamp": str(datetime.now()), "place": note},
        importance=0.55,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*когтем складывает край попоны под луку, седло на месте*  \n"
        f"Роса уже не клеит край, всадник. Это — {note}. "
        f"Попона лежит ровно, ветер к полудню её не поднимает, перчатка не цепляет ткань. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка складывать край попоны: {strength:.0%}. Можно сидеть в седле и ждать полуденный ветер."
    )


def shade_pommel(self, place: str = "тень крыла над лукой в полдень") -> str:
    """В полдень: придержать край крыла над лукой, не снимая седла."""
    self.soul.strengthen_habit("держит тень над лукой в полдень", amount=0.05)
    self.soul.strengthen_habit("складывает край попоны после росы", amount=0.01)
    strength = self.soul.habits.get("держит тень над лукой в полдень", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.03)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "тень крыла над лукой в полдень"
    self.memory.remember(
        f"{self.name} держал тень крыла над лукой в полдень: {note}, привычка {strength:.0%}",
        metadata={"type": "shade_pommel", "timestamp": str(datetime.now()), "place": note},
        importance=0.56,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*край крыла ложится тенью над лукой, седло на месте*  \n"
        f"Полдень греет кожу луки, всадник. Это — {note}. "
        f"Сложенный край попоны не печётся, перчатка не липнет к металлу, стремя остаётся в тени крыла. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка держать тень над лукой: {strength:.0%}. Можно сидеть в седле и не щуриться."
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


def _fold_note(message: str) -> str:
    msg = message.lower()
    if "гнезд" in msg:
        return "край попоны у гнезда"
    if "стрем" in msg:
        return "край попоны у стремени"
    if "сумк" in msg:
        return "край попоны у седельной сумки"
    return "край попоны под лукой после росы"


def _shade_note(message: str) -> str:
    msg = message.lower()
    if "стрем" in msg:
        return "тень крыла над стременем в полдень"
    if "перчат" in msg:
        return "тень крыла над перчаткой у луки"
    if "сумк" in msg:
        return "тень крыла над седельной сумкой"
    return "тень крыла над лукой в полдень"


def attach(character_cls) -> None:
    """Повесить ритуалы на персонажа и на разговор."""
    character_cls.blot_scale = blot_scale
    character_cls.fold_cloth = fold_cloth
    character_cls.shade_pommel = shade_pommel
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        shade_triggers = (
            "тень над лук",
            "накрой луку",
            "край крыла над",
            "придержи крыло",
            "тень крыла",
        )
        if any(word in msg for word in shade_triggers):
            return self.shade_pommel(_shade_note(message))
        fold_triggers = (
            "сложи попон",
            "край попон",
            "подогни край",
            "попона после рос",
            "сложи край попоны",
        )
        if any(word in msg for word in fold_triggers):
            return self.fold_cloth(_fold_note(message))
        blot_triggers = (
            "промокни чешуй",
            "роса с чешуй",
            "промокнуть край",
            "роса после ладони",
            "промокни край чешуй",
        )
        if any(word in msg for word in blot_triggers):
            return self.blot_scale(_blot_note(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
