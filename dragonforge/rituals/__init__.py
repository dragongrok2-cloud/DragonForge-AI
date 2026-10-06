"""Утренние, полуденные и послеполуденные ритуалы, которые крепятся на персонаже."""

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




def ease_wing(self, place: str = "край крыла после полуденной тени") -> str:
    """После полудня: чуть опустить край крыла, не снимая седла."""
    self.soul.strengthen_habit("опускает край крыла после полуденной тени", amount=0.05)
    self.soul.strengthen_habit("держит тень над лукой в полдень", amount=0.01)
    strength = self.soul.habits.get("опускает край крыла после полуденной тени", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "край крыла после полуденной тени"
    self.memory.remember(
        f"{self.name} опустил край крыла после полуденной тени: {note}, привычка {strength:.0%}",
        metadata={"type": "ease_wing", "timestamp": str(datetime.now()), "place": note},
        importance=0.56,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*чуть опускает край крыла, тень с луки сходит мягко, седло на месте*  \n"
        f"Полдень уже не жжёт, всадник. Это — {note}. "
        f"Прохладный воздух проходит под крылом, сложенный край попоны не поднимается, перчатка не липнет. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка опускать край крыла: {strength:.0%}. Можно сидеть в седле и дышать послеполуденным ветром."
    )




def settle_stirrup(self, place: str = "стремя после опущенного края") -> str:
    """После опущенного края крыла: выровнять стремя, не снимая седла."""
    self.soul.strengthen_habit("выравнивает стремя после опущенного края", amount=0.05)
    self.soul.strengthen_habit("опускает край крыла после полуденной тени", amount=0.01)
    strength = self.soul.habits.get("выравнивает стремя после опущенного края", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "стремя после опущенного края"
    self.memory.remember(
        f"{self.name} выровнял стремя после опущенного края: {note}, привычка {strength:.0%}",
        metadata={"type": "settle_stirrup", "timestamp": str(datetime.now()), "place": note},
        importance=0.56,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*когтем выравнивает стремя, край крыла уже ниже, седло на месте*  \n"
        f"Ветер после тени качнул стремя, всадник. Это — {note}. "
        f"Нога снова стоит ровно, ремень не крутит, опущенный край крыла не задевает пряжку. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка выравнивать стремя: {strength:.0%}. Можно сидеть в седле и ехать послеполуденным ветром."
    )



def snug_buckle(self, place: str = "пряжка после ровного стремени") -> str:
    """После ровного стремени: прижать пряжку подпруги, не снимая седла."""
    self.soul.strengthen_habit("прижимает пряжку после ровного стремени", amount=0.05)
    self.soul.strengthen_habit("выравнивает стремя после опущенного края", amount=0.01)
    strength = self.soul.habits.get("прижимает пряжку после ровного стремени", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "пряжка после ровного стремени"
    self.memory.remember(
        f"{self.name} прижал пряжку после ровного стремени: {note}, привычка {strength:.0%}",
        metadata={"type": "snug_buckle", "timestamp": str(datetime.now()), "place": note},
        importance=0.57,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*когтем прижимает пряжку подпруги, стремя уже ровное, седло на месте*  \n"
        f"Послеполуденный ветер ещё звенит металлом, всадник. Это — {note}. "
        f"Пряжка села в кожу, ремень не болтается, ровное стремя не задевает край. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка прижимать пряжку: {strength:.0%}. Можно сидеть в седле и не слушать звон."
    )



def tuck_strap(self, place: str = "конец ремня после тихой пряжки") -> str:
    """После прижатой пряжки: подвернуть свободный конец ремня, не снимая седла."""
    self.soul.strengthen_habit("подворачивает конец ремня после тихой пряжки", amount=0.05)
    self.soul.strengthen_habit("прижимает пряжку после ровного стремени", amount=0.01)
    strength = self.soul.habits.get("подворачивает конец ремня после тихой пряжки", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "конец ремня после тихой пряжки"
    self.memory.remember(
        f"{self.name} подвернул конец ремня после тихой пряжки: {note}, привычка {strength:.0%}",
        metadata={"type": "tuck_strap", "timestamp": str(datetime.now()), "place": note},
        importance=0.57,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*когтем подворачивает свободный конец ремня под пряжку, седло на месте*  \n"
        f"Пряжка уже молчит, а хвост ремня ещё хлопает, всадник. Это — {note}. "
        f"Конец лёг под кожу, ветер его не поднимает, тихая пряжка не звенит. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка подворачивать конец ремня: {strength:.0%}. Можно сидеть в седле и не слушать хлопки."
    )


def _tuck_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "левый конец ремня после тихой пряжки"
    if "прав" in msg:
        return "правый конец ремня после тихой пряжки"
    if "рек" in msg:
        return "конец ремня над рекой после тихой пряжки"
    return "конец ремня после тихой пряжки"


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



def _ease_note(message: str) -> str:
    msg = message.lower()
    if "стрем" in msg:
        return "край крыла над стременем после тени"
    if "перчат" in msg:
        return "край крыла над перчаткой после тени"
    if "рек" in msg:
        return "край крыла над рекой после полуденной тени"
    return "край крыла после полуденной тени"



def _settle_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "левое стремя после опущенного края"
    if "прав" in msg:
        return "правое стремя после опущенного края"
    if "рек" in msg:
        return "стремя над рекой после опущенного края"
    return "стремя после опущенного края"



def _snug_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "левая пряжка после ровного стремени"
    if "прав" in msg:
        return "правая пряжка после ровного стремени"
    if "рек" in msg:
        return "пряжка над рекой после ровного стремени"
    return "пряжка после ровного стремени"


def attach(character_cls) -> None:
    """Повесить ритуалы на персонажа и на разговор."""
    character_cls.blot_scale = blot_scale
    character_cls.fold_cloth = fold_cloth
    character_cls.shade_pommel = shade_pommel
    character_cls.ease_wing = ease_wing
    character_cls.settle_stirrup = settle_stirrup
    character_cls.snug_buckle = snug_buckle
    character_cls.tuck_strap = tuck_strap
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        tuck_triggers = (
            "подогни ремень",
            "конец ремня",
            "хвост подпруги",
            "ремень не хлопает",
        )
        if any(word in msg for word in tuck_triggers):
            return self.tuck_strap(_tuck_note(message))
        snug_triggers = (
            "прижми пряжку",
            "пряжка после стремени",
            "подпруга после стремени",
            "пряжка не звенит",
        )
        if any(word in msg for word in snug_triggers):
            return self.snug_buckle(_snug_note(message))
        settle_triggers = (
            "выровняй стремя",
            "поправь стремя после",
            "стремя после края",
            "стремя после крыла",
        )
        if any(word in msg for word in settle_triggers):
            return self.settle_stirrup(_settle_note(message))
        ease_triggers = (
            "опусти крыло",
            "опусти край",
            "после тени",
            "прохладный край",
            "край после полуд",
        )
        if any(word in msg for word in ease_triggers):
            return self.ease_wing(_ease_note(message))
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