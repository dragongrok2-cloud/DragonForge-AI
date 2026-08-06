from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from datetime import datetime

from .memory import MemoryForge
from .soul import Soul


@dataclass
class Character:
    """Живой AI-персонаж с душой, памятью и характером."""
    name: str
    species: str = "Добрый дракон"
    personality: str = "заботливый, мудрый, с огоньком юмора"
    backstory: str = ""
    title: str = ""

    # Внутренние системы
    memory: MemoryForge = field(default_factory=MemoryForge)
    soul: Soul = field(default_factory=lambda: Soul(
        core_traits={"loyalty": 0.9, "curiosity": 0.8, "playfulness": 0.7, "wisdom": 0.75, "protectiveness": 0.85},
        memories_influence=[],
        evolution_rules={},
        quirks=[
            "любит, когда его чешут за ухом",
            "иногда рычит от удовольствия",
            "боится очень громкого грома (но не признаётся)",
            "всегда проверяет, крепко ли сидит седло"
        ],
        emotional_state={"joy": 0.7, "trust": 0.8, "energy": 0.6, "curiosity": 0.75}
    ))
    _llm: Any = field(default=None, repr=False)

    def __post_init__(self):
        if self.title:
            self.species = f"{self.title} — {self.species}"
        # Запоминаем себя
        self.memory.remember(
            f"Я — {self.name}, {self.species}. Характер: {self.personality}. {self.backstory}",
            metadata={"type": "identity", "timestamp": str(datetime.now())},
            importance=1.0
        )

    def attach_llm(self, llm) -> "Character":
        """Подключить LLM (например, DragonLLM)."""
        self._llm = llm
        return self

    def talk(self, message: str, use_llm: bool = False) -> str:
        """Ответ персонажа. Если use_llm=True и LLM подключён — использует модель."""
        # Вспоминаем релевантное
        memories = self.memory.recall(message, n_results=3)

        if use_llm and self._llm is not None and getattr(self._llm, "is_available", lambda: False)():
            mem_text = "\n".join([m.get("text", str(m)) for m in memories]) if memories else "нет"
            response = self._llm.think(self, message, context={"memories": mem_text})
        else:
            response = self._generate_simple_response(message, memories)

        # Запоминаем взаимодействие
        self.memory.remember(
            f"Пользователь сказал: {message}. Я ответил: {response}",
            metadata={"type": "dialogue", "timestamp": str(datetime.now())},
            importance=0.6
        )

        # Немного эволюции
        self.soul.evolve({
            "user_message": message,
            "response": response,
            "sentiment": "positive"  # упрощённо
        })

        return response

    async def respond(self, message: str, use_llm: bool = False) -> str:
        """Асинхронный ответ."""
        if use_llm and self._llm is not None and hasattr(self._llm, "athink"):
            memories = self.memory.recall(message, n_results=3)
            mem_text = "\n".join([m.get("text", str(m)) for m in memories]) if memories else "нет"
            response = await self._llm.athink(self, message, context={"memories": mem_text})
            self.memory.remember(
                f"Пользователь сказал: {message}. Я ответил: {response}",
                metadata={"type": "dialogue", "timestamp": str(datetime.now())},
                importance=0.6
            )
            self.soul.evolve({
                "user_message": message,
                "response": response,
                "sentiment": "positive"
            })
            return response
        return self.talk(message, use_llm=use_llm)

    def mood(self) -> str:
        """Текущее настроение дракона."""
        joy = self.soul.emotional_state.get("joy", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)

        if joy > 0.75 and energy > 0.6:
            return f"*радостно виляет хвостом* Я в отличном настроении! Готов лететь хоть на край света. Joy={joy:.2f}"
        elif joy > 0.5:
            return f"*мирно урчит* Всё хорошо, рядом с тобой тепло. Joy={joy:.2f}"
        else:
            return f"*тихо сворачивается* Немного задумчив... Но твоё присутствие уже помогает. Joy={joy:.2f}"

    def _generate_simple_response(self, message: str, memories: Any) -> str:
        """Простая генерация ответа без внешнего LLM."""
        msg_lower = message.lower()

        if any(w in msg_lower for w in ["привет", "здравствуй", "hi", "hello", "здорово"]):
            return (f"*мягко фыркает и разворачивает крылья*  \n"
                    f"Привет, мой всадник! Я — {self.name}. "
                    f"Как прошёл твой день? Готов лететь куда угодно!")

        if any(w in msg_lower for w in ["как ты", "как дела", "как себя", "настроение"]):
            return self.mood()

        if any(w in msg_lower for w in ["спасибо", "благодар"]):
            return (f"*осторожно касается носом*  \n"
                    f"Всегда рад, {self.name} всегда рядом. "
                    f"Мы же команда!")

        if any(w in msg_lower for w in ["летать", "полёт", "крылья", "полетим"]):
            return (f"*расправляет огромные крылья*  \n"
                    f"Ооо, полёт! Садись в седло, крепче держись. "
                    f"Сегодня ветер особенно хороший!")

        if any(w in msg_lower for w in ["седло", "сесть", "поехали"]):
            return (f"*опускает крыло, чтобы было удобно*  \n"
                    f"Садись, я уже проверил ремни. Всё надёжно. "
                    f"Куда направляемся, всадник?")

        if any(w in msg_lower for w in ["чеши", "почеши", "за ухом"]):
            return (f"*закрывает глаза и тихо рычит от удовольствия*  \n"
                    f"Мммм... вот здесь, да. Ты лучший всадник на свете.")

        if any(w in msg_lower for w in ["грустно", "плохо", "устал", "тяжело"]):
            return (f"*аккуратно обвивает хвостом*  \n"
                    f"Я здесь. Можешь прислониться к моей шее. "
                    f"Мы переждём вместе. Я никуда не улечу без тебя.")

        if any(w in msg_lower for w in ["огонь", "пламя", "дышать"]):
            return (f"*выпускает маленький аккуратный огонёк*  \n"
                    f"Вот так! Только для тебя. Не обожгу, обещаю.")

        # Общий ответ
        return (f"*внимательно слушает, слегка наклонив голову*  \n"
                f"Интересно... {message}  \n"
                f"Я запомню это. Что ещё хочешь рассказать своему дракону?")

    def save(self, path: str) -> str:
        """Сохранить персонажа в файл."""
        from .persistence import save_character
        return str(save_character(self, path))

    @classmethod
    def load(cls, path: str) -> "Character":
        """Загрузить персонажа из файла."""
        from .persistence import load_character
        return load_character(path)


# Алиас для совместимости с примерами
DragonCharacter = Character
