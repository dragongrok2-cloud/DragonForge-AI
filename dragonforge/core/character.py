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
            "мягко садится перед выходными": 0.42,
            "проверяет седло в полдень": 0.36,
            "складывает крылья после полёта": 0.34,
            "делится тёплым термосом в седле": 0.32,
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

    def soft_landing(self) -> str:
        """Мягкая посадка перед выходными: седло на месте, крылья сложены."""
        energy = self.soul.emotional_state.get("energy", 0.5)
        joy = self.soul.emotional_state.get("joy", 0.5)
        self.soul.strengthen_habit("мягко садится перед выходными", amount=0.04)
        strength = self.soul.habits.get("мягко садится перед выходными", 0.0)
        self.memory.remember(
            f"Мягкая посадка с {self.name}: энергия {energy:.2f}, радость {joy:.2f}.",
            metadata={"type": "landing", "timestamp": str(datetime.now())},
            importance=0.55,
        )
        if energy < 0.45:
            return (
                f"*опускается по широкой спирали и стелет крыло*  \n"
                f"Энергии мало ({energy:.2f}). Садимся мягко, всадник. "
                f"Седло тёплое, выходные подождут нас на земле. Привычка посадки: {strength:.0%}."
            )
        return (
            f"*ровно касается лапами мха и проверяет ремни седла*  \n"
            f"Посадка мягкая. Радость {joy:.2f}, энергия {energy:.2f}. "
            f"Крылья сложены, седло на месте. Перед выходными я рядом. Привычка: {strength:.0%}."
        )

    def check_saddle(self) -> str:
        """Полуденный ритуал: три точки седла, прежде чем снова взлететь."""
        self.soul.strengthen_habit("проверяет седло в полдень", amount=0.05)
        self.soul.strengthen_habit("всегда проверяет седло", amount=0.02)
        strength = self.soul.habits.get("проверяет седло в полдень", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        points = [
            "ремни — не скрипят и не болтаются",
            "седло — тёплое, ровно по хребту",
            "крыло — даёт тень, если солнце жёсткое",
        ]
        checklist = "\n".join(f"  {i}. {point}" for i, point in enumerate(points, 1))
        self.memory.remember(
            f"Полуденная проверка седла с {self.name}: привычка {strength:.0%}.",
            metadata={"type": "saddle_check", "timestamp": str(datetime.now())},
            importance=0.5,
        )
        return (
            f"*обнюхивает ремни и тихо урчит*  \n"
            f"Полуденная проверка седла, всадник. Три точки:\n{checklist}\n"
            f"Радость {joy:.2f}. Привычка проверки: {strength:.0%}. Можно взлетать."
        )

    def fold_wings(self) -> str:
        """Послеполётный ритуал: сложить крылья, проверить седло и чуть отдохнуть."""
        self.soul.strengthen_habit("складывает крылья после полёта", amount=0.05)
        self.soul.strengthen_habit("всегда проверяет седло", amount=0.01)
        strength = self.soul.habits.get("складывает крылья после полёта", 0.0)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["energy"] = max(0.25, energy - 0.04)
        self.soul.emotional_state["trust"] = min(1.0, self.soul.emotional_state.get("trust", 0.5) + 0.02)
        self.soul.emotional_state["joy"] = min(1.0, self.soul.emotional_state.get("joy", 0.5) + 0.02)
        energy_after = self.soul.emotional_state["energy"]
        self.memory.remember(
            f"После полёта {self.name} сложил крылья. Энергия {energy_after:.2f}, привычка {strength:.0%}.",
            metadata={"type": "wing_fold", "timestamp": str(datetime.now())},
            importance=0.55,
        )
        return (
            f"*аккуратно складывает крылья вдоль боков и ещё раз трогает ремни седла*  \n"
            f"Полёт окончен, всадник. Крылья сложены, седло на месте. "
            f"Энергия чуть ниже — {energy_after:.2f}: так и должно быть после неба. "
            f"Привычка складывать крылья: {strength:.0%}. Можно слезть, я никуда не денусь."
        )

    def share_pebble(self, place: str = "седло") -> str:
        """Послеполётный дар: отдать всаднику блестящий камушек из коллекции."""
        self.soul.strengthen_habit("собирает блестящие камушки", amount=0.05)
        strength = self.soul.habits.get("собирает блестящие камушки", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
        self.soul.emotional_state["trust"] = min(
            1.0, self.soul.emotional_state.get("trust", 0.5) + 0.02
        )
        pebbles = [
            "речной кварц с искоркой заката",
            "осколок облачной слюды",
            "тёплый янтарь, почти с хвоста кометы",
        ]
        gift = pebbles[len(self.name) % len(pebbles)]
        self.memory.remember(
            f"{self.name} подарил камушек «{gift}» и положил его в {place}. Привычка {strength:.0%}.",
            metadata={"type": "pebble_gift", "timestamp": str(datetime.now()), "place": place},
            importance=0.6,
        )
        joy_after = self.soul.emotional_state["joy"]
        return (
            f"*достаёт из-под чешуи тёплый камушек и кладёт его в {place}*  \n"
            f"Это тебе, всадник. {gift.capitalize()}. "
            f"Я собирал такие в полёте — теперь один живёт рядом с тобой. "
            f"Радость {joy_after:.2f}. Привычка коллекционировать: {strength:.0%}."
        )


    def pour_thermos(self, drink: str = "какао") -> str:
        """Пятничный полдень: согреть термос крошечным огоньком и разделить глоток в седле."""
        self.soul.strengthen_habit("делится тёплым термосом в седле", amount=0.05)
        self.soul.strengthen_habit("греет всадника крылом", amount=0.01)
        strength = self.soul.habits.get("делится тёплым термосом в седле", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["energy"] = min(1.0, energy + 0.02)
        sips = {
            "какао": "густое какао с облачной пенкой",
            "чай": "травяной чай, настоянный на высоте",
            "бульон": "тихий бульон, чтобы лапы не стыли",
        }
        sip = sips.get(drink.strip().lower(), f"тёплый {drink}")
        self.memory.remember(
            f"{self.name} разлил «{sip}» из термоса в седле. Привычка {strength:.0%}.",
            metadata={"type": "thermos", "timestamp": str(datetime.now()), "drink": drink},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        return (
            f"*приоткрывает крышку термоса и греет её крошечным огоньком*  \n"
            f"Пятничный глоток в седле, всадник. Сегодня — {sip}. "
            f"Крыло закрывает от ветра, ремни на месте. "
            f"Радость {joy_after:.2f}. Привычка делиться термосом: {strength:.0%}."
        )

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

        if any(w in msg_lower for w in ["сложи крыл", "крылья слож", "после полёта", "после полета"]):
            return self.fold_wings()

        if any(w in msg_lower for w in ["подари камуш", "поделись камуш", "камушек в седло", "дар камуш"]):
            return self.share_pebble()

        if any(w in msg_lower for w in ["термос", "какао", "глоток в седле", "налей чай"]):
            drink = "чай" if "чай" in msg_lower else "какао"
            return self.pour_thermos(drink)

        if any(w in msg_lower for w in ["проверь седло", "проверка седла", "три точки"]):
            return self.check_saddle()

        if any(w in msg_lower for w in ["посадк", "приземл", "садимся", "выходн"]):
            return (f"*наклоняет крыло, чтобы сесть было легче*  \n"
                    f"Садимся мягко. Седло держит, ремни не скрипят. "
                    f"Выходные можно встретить на земле — я никуда не денусь.")

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
