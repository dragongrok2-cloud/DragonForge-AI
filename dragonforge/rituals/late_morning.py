"""Позднеутренний ритуал: цвет нитки на уже посчитанных стежках."""

from datetime import datetime


def name_thread(self, place: str = "цвет нитки на стежках к позднему утру") -> str:
    """После счёта стежков: назвать цвет нитки, не разворачивая подворот и не снимая седла."""
    self.soul.strengthen_habit("называет цвет нитки на стежках к позднему утру", amount=0.05)
    self.soul.strengthen_habit("считает стежки на тёплой складке утром", amount=0.01)
    strength = self.soul.habits.get("называет цвет нитки на стежках к позднему утру", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "цвет нитки на стежках к позднему утру"
    self.memory.remember(
        f"{self.name} назвал цвет нитки на стежках к позднему утру: {note}, привычка {strength:.0%}",
        metadata={"type": "name_thread", "timestamp": str(datetime.now()), "place": note},
        importance=0.57,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*к позднему утру называет цвет нитки на стежках, подворот не разворачивает, седло на месте*  \n"
        f"Стежки уже посчитаны, всадник. Это — {note}. "
        f"Нитка тёплая, медовая, шов не расходится, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка называть цвет нитки: {strength:.0%}. Можно садиться в седло и не гадать, какого цвета шов."
    )


def _name_thread_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "цвет нитки на левых стежках к позднему утру"
    if "прав" in msg:
        return "цвет нитки на правых стежках к позднему утру"
    if "рек" in msg:
        return "цвет нитки на стежках над рекой к позднему утру"
    return "цвет нитки на стежках к позднему утру"




def tuck_thread(self, place: str = "конец нитки под стежками к полудню") -> str:
    """После названного цвета: прижать свободный конец нитки, не разворачивая подворот и не снимая седла."""
    self.soul.strengthen_habit("прижимает конец нитки к полудню", amount=0.05)
    self.soul.strengthen_habit("называет цвет нитки на стежках к позднему утру", amount=0.01)
    strength = self.soul.habits.get("прижимает конец нитки к полудню", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "конец нитки под стежками к полудню"
    self.memory.remember(
        f"{self.name} прижал конец нитки к полудню: {note}, привычка {strength:.0%}",
        metadata={"type": "tuck_thread", "timestamp": str(datetime.now()), "place": note},
        importance=0.58,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*к полудню прижимает конец нитки когтем под стежки, подворот не разворачивает, седло на месте*  \n"
        f"Цвет уже назван, всадник. Это — {note}. "
        f"Медовый хвостик лёг под шов, ветер его не тянет, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка прижимать конец нитки: {strength:.0%}. Можно садиться в седло и не ловить торчащую нитку."
    )


def _tuck_thread_note(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "конец нитки под левыми стежками к полудню"
    if "прав" in msg:
        return "конец нитки под правыми стежками к полудню"
    if "рек" in msg:
        return "конец нитки под стежками над рекой к полудню"
    return "конец нитки под стежками к полудню"


def attach_late(character_cls) -> None:
    """Повесить позднеутренний ритуал поверх уже прикреплённых разговоров."""
    character_cls.name_thread = name_thread
    character_cls.tuck_thread = tuck_thread
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        tuck_triggers = (
            "прижми конец нит",
            "конец нитки",
            "подоткни нит",
            "нитка не торч",
            "хвостик нит",
        )
        thread_triggers = (
            "назови цвет нит",
            "цвет нитки",
            "нитка на стеж",
            "какого цвета шов",
            "нитка у пряж",
        )
        if any(word in msg for word in tuck_triggers):
            return self.tuck_thread(_tuck_thread_note(message))
        if any(word in msg for word in thread_triggers):
            return self.name_thread(_name_thread_note(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
