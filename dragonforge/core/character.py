from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from datetime import datetime

from .memory import MemoryForge
from .soul import Soul


@dataclass
class Character:
    """Живой AI-персонаж с душой, памятью, привычками и характером."""
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
        habits={
            "всегда проверяет седло": 0.85,
            "любит почесывания за ухом": 0.80,
            "рычит от удовольствия": 0.70,
            "боится громкого грома": 0.45,
            "греет всадника крылом": 0.60,
            "собирает блестящие камушки": 0.35,
            "любит рассветы над облаками": 0.40,
            "делится утренним огоньком": 0.30,
        },
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
        memories = self.memory.recall(message, n_results=3)

        if use_llm and self._llm is not None and getattr(self._llm, "is_available", lambda: False)():
            mem_text = "\n".join([m.get("text", str(m)) for m in memories]) if memories else "нет"
            response = self._llm.think(self, message, context={"memories": mem_text})
        else:
            response = self._generate_simple_response(message, memories)

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

        if joy > 0.75 and energy > 0.6:
            return f"*радостно виляет хвостом* Я в отличном настроении! Готов лететь хоть на край света. Joy={joy:.2f}"
        elif joy > 0.5:
            return f"*мирно урчит* Всё хорошо, рядом с тобой тепло. Joy={joy:.2f}"
        else:
            return f"*тихо сворачивается* Немного задумчив... Но твоё присутствие уже помогает. Joy={joy:.2f}"

    def describe_soul(self) -> str:
        """Краткое описание текущей души дракона."""
        return self.soul.describe()

    def habits(self) -> str:
        """Показать все привычки дракона с их силой."""
        return self.soul.describe_habits()

    def _generate_simple_response(self, message: str, memories: Any) -> str:
        """Простая генерация ответа без внешнего LLM. Учитывает сильные привычки."""
        msg_lower = message.lower()
        strong = self.soul.get_strong_habits(0.65)

        if any(w in msg_lower for w in ["привет", "здравствуй", "hi", "hello", "здорово", "хай", "доброе утро"]):
            extra = ""
            if "всегда проверяет седло" in strong:
                extra = " Седло уже проверено, кстати."
            return (f"*мягко фыркает и разворачивает крылья*  \n"
                    f"Привет, мой всадник! Я — {self.name}. "
                    f"Как прошёл твой день? Готов лететь куда угодно!{extra}")

        if any(w in msg_lower for w in ["как ты", "как дела", "как себя", "настроение"]):
            return self.mood()

        if any(w in msg_lower for w in ["спасибо", "благодар", "мерси"]):
            return (f"*осторожно касается носом*  \n"
                    f"Всегда рад, {self.name} всегда рядом. "
                    f"Мы же команда!")

        if any(w in msg_lower for w in ["рассвет", "рассветн", "восход"]):
            extra = ""
            if "любит рассветы над облаками" in self.soul.habits:
                extra = " Это моё любимое время суток — небо ещё тихое, а крылья уже горячие."
            return (f"*поднимает голову к розовому небу*{extra}  \n"
                    f"Садись. Седло тёплое. Мы успеем к первому лучу.")

        if any(w in msg_lower for w in ["пикник", "чай"]):
            spark = ""
            if "делится утренним огоньком" in self.soul.habits:
                spark = " Я подогрею чай маленьким огоньком — ровно столько, чтобы не вскипел."
            return (f"*аккуратно расправляет крыло как скатерть*{spark}  \n"
                    f"Облако держит. Садись рядом. У нас есть время.")

        if any(w in msg_lower for w in ["дождь", "ливень", "моросит"]):
            return (f"*прикрывает тебя крылом, как навесом*  \n"
                    f"Дождь может шуметь. Под крылом сухо. Я не улечу.")

        if any(w in msg_lower for w in ["летать", "полёт", "крылья", "полетим", "полетай"]):
            saddle_note = ""
            if "всегда проверяет седло" in strong and strong["всегда проверяет седло"] > 0.8:
                saddle_note = " Я уже трижды проверил ремни."
            return (f"*расправляет огромные крылья*  \n"
                    f"Ооо, полёт! Садись в седло, крепче держись.{saddle_note} "
                    f"Сегодня ветер особенно хороший!")

        if any(w in msg_lower for w in ["седло", "сесть", "поехали", "в седло"]):
            return (f"*опускает крыло, чтобы было удобно*  \n"
                    f"Садись, я уже проверил ремни. Всё надёжно. "
                    f"Куда направляемся, всадник?")

        if any(w in msg_lower for w in ["чеши", "почеши", "за ухом", "почеши за", "ушко"]):
            intensity = ""
            if "любит почесывания за ухом" in strong and strong["любит почесывания за ухом"] > 0.85:
                intensity = " *особенно громко рычит от счастья*"
            return (f"*закрывает глаза и тихо рычит от удовольствия*{intensity}  \n"
                    f"Мммм... вот здесь, да. Ты лучший всадник на свете.")

        if any(w in msg_lower for w in ["грустно", "плохо", "устал", "тяжело", "устала"]):
            wing = ""
            if "греет всадника крылом" in strong:
                wing = " *аккуратно накрывает тебя крылом*"
            return (f"*аккуратно обвивает хвостом*{wing}  \n"
                    f"Я здесь. Можешь прислониться к моей шее. "
                    f"Мы переждём вместе. Я никуда не улечу без тебя.")

        if any(w in msg_lower for w in ["огонь", "пламя", "дышать", "огнём", "огонёк", "огонек"]):
            return (f"*выпускает маленький аккуратный огонёк*  \n"
                    f"Вот так! Только для тебя. Не обожгу, обещаю.")

        if any(w in msg_lower for w in ["люблю", "любишь", "любимый", "дорогой"]):
            return (f"*тепло урчит и слегка прижимается*  \n"
                    f"И я тебя, всадник. Ты — моё самое важное сокровище.")

        if any(w in msg_lower for w in ["голодный", "есть", "еда", "покорми"]):
            return (f"*с интересом наклоняет голову*  \n"
                    f"Я бы не отказался от чего-нибудь вкусного... "
                    f"Но ещё больше я люблю, когда ты рядом.")

        if any(w in msg_lower for w in ["спать", "отдых", "усни", "спокойной"]):
            return (f"*сворачивается калачиком рядом*  \n"
                    f"Спокойной ночи. Я буду сторожить твой сон. "
                    f"Крылья рядом, если понадоблюсь.")

        if any(w in msg_lower for w in ["кто ты", "расскажи о себе", "что ты такое"]):
            return (f"*важно выпрямляется*  \n"
                    f"Я — {self.name}, {self.species}. "
                    f"Характер: {self.personality}. {self.backstory or 'Просто твой верный дракон.'}")

        if any(w in msg_lower for w in ["привычк", "привычки", "что ты любишь"]):
            return self.habits()

        if any(w in msg_lower for w in ["гром", "гроза", "молния"]):
            if "боится громкого грома" in strong and strong["боится громкого грома"] > 0.5:
                return (f"*чуть съёживается и старается выглядеть храбро*  \n"
                        f"Гром? Ну... я не боюсь. Просто... стою ближе к тебе. На всякий случай.")
            return (f"*спокойно смотрит на небо*  \n"
                    f"Гроза — это просто небо разговаривает. Я рядом.")

        if any(w in msg_lower for w in ["камень", "камушек", "блестит", "сокровище"]):
            if "собирает блестящие камушки" in strong:
                return (f"*заинтересованно наклоняет голову и тихо урчит*  \n"
                        f"Ооо, блестящий... Можно я его... ну, просто подержу? "
                        f"У меня уже есть маленькая коллекция.")
            return (f"*с любопытством смотрит*  \n"
                    f"Красивый камушек. Хочешь, положим его в надёжное место?")

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
