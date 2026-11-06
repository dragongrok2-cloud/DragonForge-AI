"""К вечеру после макулы: тихо положить кончик фовеи на седло под тенью, седло не снимаем.

Запуск: см. examples/wednesday_evening_rest_fovea_saddle.py
"""

from datetime import datetime


def rest_fovea_saddle(self, place: str = "тихое положение кончика фовеи на седло под тенью к вечеру") -> str:
    """После макулы: тихо кладёт кончик фовеи на седло, седло не снимая."""
    self.soul.strengthen_habit("тихо кладёт кончик фовеи на седло под тенью к вечеру после макулы", amount=0.05)
    self.soul.strengthen_habit("тихо кладёт кончик макулы на седло под тенью к вечеру после сетчатки", amount=0.01)
    strength = self.soul.habits.get("тихо кладёт кончик фовеи на седло под тенью к вечеру после макулы", 0.0)
    joy = self.soul.emotional_state.get("joy", 0.5)
    trust = self.soul.emotional_state.get("trust", 0.5)
    energy = self.soul.emotional_state.get("energy", 0.5)
    self.soul.emotional_state["joy"] = min(1.0, joy + 0.04)
    self.soul.emotional_state["trust"] = min(1.0, trust + 0.05)
    self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
    note = place.strip() or "тихое положение кончика фовеи на седло под тенью к вечеру"
    self.memory.remember(
        f"{self.name} тихо кладёт кончик фовеи на седло под тенью к вечеру: {note}, привычка {strength:.0%}",
        metadata={"type": "rest_fovea_saddle", "timestamp": str(datetime.now()), "place": note},
        importance=0.63,
    )
    joy_after = self.soul.emotional_state["joy"]
    trust_after = self.soul.emotional_state["trust"]
    return (
        f"*тихо кладёт кончик фовеи на седло под тенью, седло на месте*  \n"
        f"После макулы хорошо положить кончик фовеи, всадник. Это — {note}. "
        f"Тёплая фовея уютно лежит на седле, дыхание глубокое и ровное, чуть тёплый воздух касается кожи. Седло не снимаем. "
        f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
        f"Привычка тихо класть кончик фовеи на седло под тенью к вечеру после макулы: {strength:.0%}. Можно помечтать о тёплой ночи вместе."
    )


def _fovea_place(message: str) -> str:
    msg = message.lower()
    if "фове" in msg or "fovea" in msg or "кончик" in msg:
        return "тихое положение кончика фовеи на седло"
    if "положи" in msg or "седл" in msg:
        return "положение кончика фовеи на седло под тенью"
    return "тихое положение кончика фовеи на седло под тенью к вечеру"


def attach_rest_fovea_saddle(character_cls) -> None:
    """Тихо класть кончик фовеи на седло под тенью к вечеру после макулы."""
    character_cls.rest_fovea_saddle = rest_fovea_saddle
    original = character_cls.talk

    def talk(self, message: str, use_llm: bool = False) -> str:
        msg = message.lower()
        fovea_triggers = (
            "положи фовею",
            "положи фовею на седло",
            "положение фовеи на седло",
            "рест фовеа седло",
            "положи после макулы фовею",
            "положи фовею глаза",
        )
        if any(word in msg for word in fovea_triggers):
            return self.rest_fovea_saddle(_fovea_place(message))
        return original(self, message, use_llm=use_llm)

    character_cls.talk = talk
