"""После полудня 9 октября: пальцы в полоске солнца, седло не снимаем."""

from datetime import datetime


def curl_fingers(self, place: str = "пальцы в полоске солнца после полудня") -> str:
    """После сдвига полоски на костяшки: согнуть пальцы, чтобы свет лёг в сгиб."""
    self.soul.strengthen_habit("сгибает пальцы в полоске солнца после полудня", amount=0.05)
    self.soul.strengthen_habit("сдвигает полоску солнца на костяшки после полудня", amount=0.01)
    strength = self.soul.habits.get("сгибает пальцы в полоске солнца после полудня", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    calm = self.soul.emotional_state.get("calm", self.soul.emotional_state.get("energy", 0.5))
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.01)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
    if "calm" in self.soul.emotional_state:
        self.soul.emotional_state["calm"] = min(1.0, calm + 0.02)
    else:
        self.soul.emotional_state["energy"] = min(1.0, self.soul.emotional_state.get("energy", 0.5) + 0.01)
    note = place.strip() or "пальцы в полоске солнца после полудня"
    fold = _fold_note(note)
    self.memory.remember(
        f"{self.name} согнул пальцы в полоске солнца после полудня: {note}, {fold}, привычка {strength:.0%}",
        metadata={"type": "curl_fingers", "timestamp": str(datetime.now()), "place": note, "fold": fold},
        importance=0.66,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*сгибает пальцы один раз, полоска солнца ложится в сгиб, фонарик не вытаскивая*  \n"
        f"Костяшки уже тёплые, всадник. Это — {note}. "
        f"Сгиб: {fold}. Пальцы можно разогнуть, пыльца не возвращается, подворот на месте. Седло не снимаем, ремни на месте. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка сгибать пальцы в полоске: {strength:.0%}. Можно сидеть в седле и держать свет в ладони."
    )


def _fold_note(note: str) -> str:
    lowered = note.lower()
    if "лев" in lowered:
        return "сгиб левой ладони на Мёде, Седло не открыто"
    if "прав" in lowered:
        return "сгиб правой ладони на Искре, Седло не открыто"
    if "рек" in lowered:
        return "сгиб над Рекой, пальцы на Мёде, Седло не открыто"
    return "сгиб ладони у Шва на Мёде, Седло не открыто"


def _fold_place(message: str) -> str:
    msg = message.lower()
    if "лев" in msg:
        return "пальцы в левой полоске солнца после полудня"
    if "прав" in msg:
        return "пальцы в правой полоске солнца после полудня"
    if "рек" in msg:
        return "пальцы в полоске солнца над рекой после полудня"
    return "пальцы в полоске солнца после полудня"


def attach_curl(character_cls) -> None:
    """Согнуть пальцы в полоске солнца после полудня."""
    character_cls.curl_fingers = curl_fingers
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        curl_triggers = (
            "согни пальц",
            "пальцы в полоск",
            "согни костяш",
            "свет в сгиб",
        )
        if any(word in msg for word in curl_triggers):
            return self.curl_fingers(_fold_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
