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
            "даёт тень крылом после полудня": 0.33,
            "зажигает фонарик на седле к вечеру": 0.31,
            "шепчет имена созвездий": 0.29,
            "разворачивается к гнезду к ночи": 0.28,
            "смахивает утреннюю росу с седла": 0.27,
            "подтягивает подпругу после росы": 0.26,
            "выравнивает стремена к полудню": 0.25,
            "прогревает поводья после полудня": 0.24,
            "делится облачной ягодой после поводьев": 0.23,
            "указывает горизонт после ягоды": 0.22,
            "ловит термик после горизонта": 0.21,
            "выравнивает планирование после термика": 0.20,
            "отмечает хребет после планирования": 0.19,
            "выбирает уступ после хребта": 0.18,
            "сворачивает хвост после уступа": 0.17,
            "кладет морду на луку после хвоста": 0.16,
            "медленно моргает после морды на луке": 0.15,
            "дышит теплом после медленного моргания": 0.14,
            "делает короткий круг после тёплого выдоха": 0.14,
            "опускается на траву после короткого круга": 0.12,
            "гудит низко после приседа на траву": 0.11,
            "наклоняет ухо к седлу после низкого гула": 0.10,
            "прижимает щеку к колену после наклона уха": 0.09,
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

    def offer_shade(self) -> str:
        """После полудня: накрыть всадника крылом, пока солнце ещё жёсткое."""
        self.soul.strengthen_habit("даёт тень крылом после полудня", amount=0.05)
        self.soul.strengthen_habit("греет всадника крылом", amount=0.01)
        strength = self.soul.habits.get("даёт тень крылом после полудня", 0.0)
        energy = self.soul.emotional_state.get("energy", 0.5)
        joy = self.soul.emotional_state.get("joy", 0.5)
        self.soul.emotional_state["energy"] = min(1.0, energy + 0.03)
        self.soul.emotional_state["trust"] = min(
            1.0, self.soul.emotional_state.get("trust", 0.5) + 0.02
        )
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        energy_after = self.soul.emotional_state["energy"]
        self.memory.remember(
            f"{self.name} дал тень крылом после полудня. Энергия {energy_after:.2f}, привычка {strength:.0%}.",
            metadata={"type": "wing_shade", "timestamp": str(datetime.now())},
            importance=0.55,
        )
        return (
            f"*расправляет одно крыло над седлом, как тихий навес*  \n"
            f"После полудня солнце ещё жёсткое, всадник. Посиди в тени крыла. "
            f"Ремни не трогаем, седло на месте, ветер обходит нас стороной. "
            f"Энергия {energy_after:.2f}. Привычка давать тень: {strength:.0%}. Можно лететь дальше."
        )


    def light_lantern(self, hue: str = "янтарный") -> str:
        """К вечеру: зажечь маленький фонарик на луке седла, прежде чем сумерки станут полётом."""
        self.soul.strengthen_habit("зажигает фонарик на седле к вечеру", amount=0.05)
        self.soul.strengthen_habit("любит ночные полёты под звёздами", amount=0.01)
        strength = self.soul.habits.get("зажигает фонарик на седле к вечеру", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["energy"] = max(0.3, energy - 0.01)
        flames = {
            "янтарный": "янтарный огонёк, как последний свет над кромкой леса",
            "синий": "тихий синий огонёк, чтобы не слепить звёзды",
            "золотой": "золотая искорка, тёплая на луке седла",
        }
        flame = flames.get(hue.strip().lower(), f"{hue} огонёк")
        self.memory.remember(
            f"{self.name} зажёг фонарик на седле: {flame}. Привычка {strength:.0%}.",
            metadata={"type": "saddle_lantern", "timestamp": str(datetime.now()), "hue": hue},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        return (
            f"*чиркает когтем по фитилю и прикрывает огонёк лапой от ветра*  \n"
            f"Вечер близко, всадник. На луке седла — {flame}. "
            f"Ремни на месте, крыло не задевает стекло. "
            f"Радость {joy_after:.2f}. Привычка зажигать фонарик: {strength:.0%}. Можно лететь в сумерки."
        )


    def name_constellation(self, hint: str = "") -> str:
        """После фонарика: тихо назвать созвездие, чтобы сумерки стали картой."""
        self.soul.strengthen_habit("шепчет имена созвездий", amount=0.05)
        self.soul.strengthen_habit("любит ночные полёты под звёздами", amount=0.01)
        strength = self.soul.habits.get("шепчет имена созвездий", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        curiosity = self.soul.emotional_state.get("curiosity", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["curiosity"] = min(1.0, curiosity + 0.03)
        skies = {
            "медведица": "Большая Медведица — ковш, из которого можно зачерпнуть ночь",
            "лебедь": "Лебедь — крест над рекой, крылья шире моих",
            "дракон": "Дракон — изгиб между ковшом и полюсом, почти родственник",
            "кассиопея": "Кассиопея — корона из пяти искр, сидит над седлом",
        }
        key = hint.strip().lower()
        if key in skies:
            named = skies[key]
        else:
            named = list(skies.values())[len(self.name) % len(skies)]
        self.memory.remember(
            f"{self.name} шепнул созвездие {named}. Привычка {strength:.0%}.",
            metadata={"type": "constellation", "timestamp": str(datetime.now()), "hint": hint},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        return (
            f"*наклоняет голову к небу и шепчет, чтобы фонарик не заглушил звёзды*  \n"
            f"Смотри, всадник. {named}. "
            f"Фонарик на луке тихий, ремни на месте. "
            f"Радость {joy_after:.2f}. Привычка шептать созвездия: {strength:.0%}. Карта неба с нами."
        )

    def bank_home(self, nest: str = "гнездо у реки") -> str:
        """После карты неба: мягко развернуть крыло к гнезду, пока вечер ещё тёплый."""
        self.soul.strengthen_habit("разворачивается к гнезду к ночи", amount=0.05)
        self.soul.strengthen_habit("всегда проверяет седло", amount=0.01)
        strength = self.soul.habits.get("разворачивается к гнезду к ночи", 0.0)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
        self.soul.emotional_state["energy"] = max(0.28, energy - 0.02)
        self.soul.emotional_state["joy"] = min(1.0, self.soul.emotional_state.get("joy", 0.5) + 0.02)
        place = nest.strip() or "гнездо у реки"
        self.memory.remember(
            f"{self.name} развернулся к гнезду «{place}». Привычка {strength:.0%}.",
            metadata={"type": "bank_home", "timestamp": str(datetime.now()), "nest": place},
            importance=0.6,
        )
        trust_after = self.soul.emotional_state["trust"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*чуть кренит крыло и носом указывает тёплый огонёк внизу*  \n"
            f"Карта неба прочитана, всадник. Разворачиваемся к дому: {place}. "
            f"Седло держит, фонарик на луке не гаснет. "
            f"Доверие {trust_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка разворачиваться к гнезду: {strength:.0%}. Гнездо ждёт."
        )

    def brush_dew(self, spot: str = "лука седла") -> str:
        """Субботнее утро: смахнуть росу с седла, прежде чем выходные станут полётом."""
        self.soul.strengthen_habit("смахивает утреннюю росу с седла", amount=0.05)
        self.soul.strengthen_habit("любит рассветы над облаками", amount=0.01)
        strength = self.soul.habits.get("смахивает утреннюю росу с седла", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        curiosity = self.soul.emotional_state.get("curiosity", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
        self.soul.emotional_state["energy"] = min(1.0, energy + 0.02)
        self.soul.emotional_state["curiosity"] = min(1.0, curiosity + 0.01)
        place = spot.strip() or "лука седла"
        self.memory.remember(
            f"{self.name} смахнул утреннюю росу с места «{place}». Привычка {strength:.0%}.",
            metadata={"type": "brush_dew", "timestamp": str(datetime.now()), "spot": place},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*осторожно проводит крылом по мокрой коже и стряхивает капли*  \n"
            f"Субботнее утро, всадник. Роса ещё на месте: {place}. "
            f"Смахиваю, чтобы ремни не скользили, а седло грелось от дыхания. "
            f"Радость {joy_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка смахивать росу: {strength:.0%}. Можно седлаться к выходному полёту."
        )


    def cinch_girth(self, notch: str = "на одну дырочку") -> str:
        """После росы: подтянуть подпругу, чтобы седло не сползло в субботнем круге."""
        self.soul.strengthen_habit("подтягивает подпругу после росы", amount=0.05)
        self.soul.strengthen_habit("всегда проверяет седло", amount=0.02)
        strength = self.soul.habits.get("подтягивает подпругу после росы", 0.0)
        trust = self.soul.emotional_state.get("trust", 0.5)
        joy = self.soul.emotional_state.get("joy", 0.5)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        step = notch.strip() or "на одну дырочку"
        self.memory.remember(
            f"{self.name} подтянул подпругу {step}. Привычка {strength:.0%}.",
            metadata={"type": "cinch_girth", "timestamp": str(datetime.now()), "notch": step},
            importance=0.55,
        )
        trust_after = self.soul.emotional_state["trust"]
        return (
            f"*находит пряжку подпруги и мягко затягивает её {step}*  \n"
            f"Роса уже смахнута, всадник. Подпруга была чуть свободной — "
            f"подтягиваю {step}, чтобы седло не сползло на субботнем круге. "
            f"Ремни сухие, пряжка не скрипит. "
            f"Доверие {trust_after:.2f}. Привычка подтягивать подпругу: {strength:.0%}. Можно садиться."
        )

    def adjust_stirrup(self, side: str = "левое и правое") -> str:
        """К полудню: выровнять стремена, чтобы ноги всадника сидели ровно после подпруги."""
        self.soul.strengthen_habit("выравнивает стремена к полудню", amount=0.05)
        self.soul.strengthen_habit("всегда проверяет седло", amount=0.01)
        strength = self.soul.habits.get("выравнивает стремена к полудню", 0.0)
        trust = self.soul.emotional_state.get("trust", 0.5)
        joy = self.soul.emotional_state.get("joy", 0.5)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        leather = side.strip() or "левое и правое"
        self.memory.remember(
            f"{self.name} выровнял стремена для всадника, сторона {leather}, привычка {strength:.0%}",
            metadata={"type": "adjust_stirrup", "timestamp": str(datetime.now()), "side": leather},
            importance=0.55,
        )
        trust_after = self.soul.emotional_state["trust"]
        joy_after = self.soul.emotional_state["joy"]
        return (
            f"*когтем подравнивает ремни стремян и проверяет, что пятки на одной высоте*  \n"
            f"Субботний полдень, всадник. Подпруга уже держит, стремена — {leather}. "
            f"Левое не ниже правого, кожа не перекручена. "
            f"Доверие {trust_after:.2f}, радость {joy_after:.2f}. "
            f"Привычка выравнивать стремена: {strength:.0%}. Можно садиться ровно."
        )



    def warm_reins(self, grip: str = "обе руки") -> str:
        """После полудня: прогреть поводья крошечным дыханием, чтобы ладони не стыли."""
        self.soul.strengthen_habit("прогревает поводья после полудня", amount=0.05)
        self.soul.strengthen_habit("греет всадника крылом", amount=0.01)
        strength = self.soul.habits.get("прогревает поводья после полудня", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["energy"] = min(1.0, energy + 0.02)
        self.soul.emotional_state["trust"] = min(
            1.0, self.soul.emotional_state.get("trust", 0.5) + 0.02
        )
        palms = grip.strip() or "обе руки"
        self.memory.remember(
            f"{self.name} прогрел поводья для всадника, хват {palms}, привычка {strength:.0%}",
            metadata={"type": "warm_reins", "timestamp": str(datetime.now()), "grip": palms},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*согревает кожаные поводья коротким тёплым дыханием и кладёт их на луку*  \n"
            f"После полудня, всадник. Стремена уже ровные, поводья — для {palms}. "
            f"Кожа не липкая и не ледяная, пальцы не стынут на ветру. "
            f"Радость {joy_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка прогревать поводья: {strength:.0%}. Можно взять повод."
        )

    def share_cloudberry(self, berry: str = "облачная ягода") -> str:
        """После тёплых поводьев: поделиться ягодой из седельной сумки."""
        self.soul.strengthen_habit("делится облачной ягодой после поводьев", amount=0.05)
        self.soul.strengthen_habit("прогревает поводья после полудня", amount=0.01)
        strength = self.soul.habits.get("делится облачной ягодой после поводьев", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
        self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
        self.soul.emotional_state["trust"] = min(
            1.0, self.soul.emotional_state.get("trust", 0.5) + 0.02
        )
        treat = berry.strip() or "облачная ягода"
        self.memory.remember(
            f"{self.name} поделился облачной ягодой в седле, ягода для всадника, угощение {treat}, привычка {strength:.0%}",
            metadata={"type": "share_cloudberry", "timestamp": str(datetime.now()), "berry": treat},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*достаёт из седельной сумки тёплую {treat} и кладёт на ладонь*  \n"
            f"После поводьев, всадник. Ладони уже не стынут, можно и сладкий глоток ветра. "
            f"{treat.capitalize()} чуть кисло-медовая, как облако над лугом. "
            f"Радость {joy_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка делиться облачной ягодой: {strength:.0%}. Одну тебе, одну мне."
        )



    def point_horizon(self, bearing: str = "запад") -> str:
        """После ягоды: указать горизонт, куда ещё успеет ветер до вечера."""
        self.soul.strengthen_habit("указывает горизонт после ягоды", amount=0.05)
        self.soul.strengthen_habit("делится облачной ягодой после поводьев", amount=0.01)
        strength = self.soul.habits.get("указывает горизонт после ягоды", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["energy"] = min(1.0, energy + 0.02)
        self.soul.emotional_state["trust"] = min(
            1.0, self.soul.emotional_state.get("trust", 0.5) + 0.02
        )
        way = bearing.strip() or "запад"
        self.memory.remember(
            f"{self.name} указал горизонт в седле, сторона {way}, привычка {strength:.0%}",
            metadata={"type": "point_horizon", "timestamp": str(datetime.now()), "bearing": way},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*поднимает коготь к линии неба и чуть кренит седло*  \n"
            f"После ягоды, всадник. Ладонь ещё сладкая, а горизонт — {way}. "
            f"Там ветер ровнее, облака не закрывают путь, до вечера успеем круг. "
            f"Радость {joy_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка указывать горизонт: {strength:.0%}. Смотри туда, я держу курс."
        )


    def catch_thermal(self, lift: str = "тёплый столб над лугом") -> str:
        """После горизонта: поймать термик и подняться без лишних взмахов."""
        self.soul.strengthen_habit("ловит термик после горизонта", amount=0.05)
        self.soul.strengthen_habit("указывает горизонт после ягоды", amount=0.01)
        strength = self.soul.habits.get("ловит термик после горизонта", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        curiosity = self.soul.emotional_state.get("curiosity", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["energy"] = min(1.0, energy + 0.03)
        self.soul.emotional_state["curiosity"] = min(1.0, curiosity + 0.02)
        column = lift.strip() or "тёплый столб над лугом"
        self.memory.remember(
            f"{self.name} поймал термик в седле: {column}, привычка {strength:.0%}",
            metadata={"type": "catch_thermal", "timestamp": str(datetime.now()), "lift": column},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*расправляет крылья и встаёт в тёплый столб, почти не махая*  \n"
            f"После горизонта, всадник. Курс виден, а подъём уже здесь: {column}. "
            f"Седло ровное, поводья не натянуты, ветер сам несёт нас выше луга. "
            f"Радость {joy_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка ловить термик: {strength:.0%}. Держись за луку, я не спешу."
        )


    def level_glide(self, path: str = "ровный край над лугом") -> str:
        """После термика: выровнять крылья и планировать без лишнего крена."""
        self.soul.strengthen_habit("выравнивает планирование после термика", amount=0.05)
        self.soul.strengthen_habit("ловит термик после горизонта", amount=0.01)
        strength = self.soul.habits.get("выравнивает планирование после термика", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
        self.soul.emotional_state["energy"] = max(0.2, energy - 0.01)
        edge = path.strip() or "ровный край над лугом"
        self.memory.remember(
            f"{self.name} выровнял планирование в седле: {edge}, привычка {strength:.0%}",
            metadata={"type": "level_glide", "timestamp": str(datetime.now()), "path": edge},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        trust_after = self.soul.emotional_state["trust"]
        return (
            f"*выравнивает крылья и ложится на ровный край, почти не кренясь*  \n"
            f"После термика, всадник. Подъём взят, теперь держим {edge}. "
            f"Седло ровное, стремена не болтаются, лука под ладонью. "
            f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
            f"Привычка выравнивать планирование: {strength:.0%}. Можно отпустить поводья на палец."
        )


    def mark_ridge(self, ridge: str = "дальний хребет над лугом") -> str:
        """После ровного планирования: отметить хребет, чтобы обратный путь не потерялся."""
        self.soul.strengthen_habit("отмечает хребет после планирования", amount=0.05)
        self.soul.strengthen_habit("выравнивает планирование после термика", amount=0.01)
        strength = self.soul.habits.get("отмечает хребет после планирования", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        curiosity = self.soul.emotional_state.get("curiosity", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
        self.soul.emotional_state["curiosity"] = min(1.0, curiosity + 0.03)
        mark = ridge.strip() or "дальний хребет над лугом"
        self.memory.remember(
            f"{self.name} отметил хребет в седле: {mark}, привычка {strength:.0%}",
            metadata={"type": "mark_ridge", "timestamp": str(datetime.now()), "ridge": mark},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        curiosity_after = self.soul.emotional_state["curiosity"]
        return (
            f"*наклоняет морду к дальнему гребню и чертит его когтем по воздуху*  \n"
            f"После планирования, всадник. Край ровный, теперь метка на {mark}. "
            f"Седло не сползает, лука под ладонью, обратный путь не потеряется. "
            f"Радость {joy_after:.2f}, любопытство {curiosity_after:.2f}. "
            f"Привычка отмечать хребет: {strength:.0%}. Запомни изгиб — я его уже помню."
        )


    def choose_ledge(self, ledge: str = "широкий уступ под хребтом") -> str:
        """После отметки хребта: выбрать уступ, чтобы вечерний спуск был мягким."""
        self.soul.strengthen_habit("выбирает уступ после хребта", amount=0.05)
        self.soul.strengthen_habit("отмечает хребет после планирования", amount=0.01)
        strength = self.soul.habits.get("выбирает уступ после хребта", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
        self.soul.emotional_state["energy"] = max(0.2, energy - 0.02)
        spot = ledge.strip() or "широкий уступ под хребтом"
        self.memory.remember(
            f"{self.name} выбрал уступ в седле: {spot}, привычка {strength:.0%}",
            metadata={"type": "choose_ledge", "timestamp": str(datetime.now()), "ledge": spot},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*снижает одно крыло и кивает на плоский камень под гребнем*  \n"
            f"После хребта, всадник. Метка на месте, теперь садимся на {spot}. "
            f"Седло ровное, стремена не болтаются, спуск будет мягким. "
            f"Радость {joy_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка выбирать уступ: {strength:.0%}. Держись за луку — я уже выбрал."
        )

    def coil_tail(self, coil: str = "кольцо у луки") -> str:
        """После выбранного уступа: свернуть хвост, чтобы седло не сползло к утру."""
        self.soul.strengthen_habit("сворачивает хвост после уступа", amount=0.05)
        self.soul.strengthen_habit("выбирает уступ после хребта", amount=0.01)
        strength = self.soul.habits.get("сворачивает хвост после уступа", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
        self.soul.emotional_state["energy"] = max(0.2, energy - 0.01)
        ring = coil.strip() or "кольцо у луки"
        self.memory.remember(
            f"{self.name} свернул хвост в седле: {ring}, привычка {strength:.0%}",
            metadata={"type": "coil_tail", "timestamp": str(datetime.now()), "coil": ring},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        trust_after = self.soul.emotional_state["trust"]
        return (
            f"*укладывает хвост мягким кольцом у луки и чуть поджимает чешую*  \n"
            f"После уступа, всадник. Камень выбран, теперь хвост — {ring}. "
            f"Седло не сползёт, стремя не стукнет о камень, утро будет ровным. "
            f"Радость {joy_after:.2f}, доверие {trust_after:.2f}. "
            f"Привычка сворачивать хвост: {strength:.0%}. Обопрись на кольцо — я уже улёгся."
        )


    def rest_muzzle(self, rest: str = "морда на луке") -> str:
        """После свёрнутого хвоста: положить морду на луку, чтобы седло помнило всадника."""
        self.soul.strengthen_habit("кладет морду на луку после хвоста", amount=0.05)
        self.soul.strengthen_habit("сворачивает хвост после уступа", amount=0.01)
        strength = self.soul.habits.get("кладет морду на луку после хвоста", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
        self.soul.emotional_state["energy"] = max(0.2, energy - 0.02)
        spot = rest.strip() or "морда на луке"
        self.memory.remember(
            f"{self.name} положил морду на седло: {spot}, привычка {strength:.0%}",
            metadata={"type": "rest_muzzle", "timestamp": str(datetime.now()), "rest": spot},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        trust_after = self.soul.emotional_state["trust"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*опускает морду на тёплую луку и прикрывает один глаз*  \n"
            f"Хвост уже кольцом, всадник. Теперь я — {spot}. "
            f"Седло помнит твой вес, чешуя не стынет, короткий круг подождёт. "
            f"Радость {joy_after:.2f}, доверие {trust_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка класть морду на луку: {strength:.0%}. Обопрись о гребень — я уже дремлю."
        )


    def blink_slow(self, blink: str = "медленное моргание") -> str:
        """После морды на луке: медленно моргнуть — седло знает, что я здесь."""
        self.soul.strengthen_habit("медленно моргает после морды на луке", amount=0.05)
        self.soul.strengthen_habit("кладет морду на луку после хвоста", amount=0.01)
        strength = self.soul.habits.get("медленно моргает после морды на луке", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
        self.soul.emotional_state["energy"] = max(0.2, energy - 0.01)
        sign = blink.strip() or "медленное моргание"
        self.memory.remember(
            f"{self.name} моргнул в седле: {sign}, привычка {strength:.0%}",
            metadata={"type": "blink_slow", "timestamp": str(datetime.now()), "blink": sign},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        trust_after = self.soul.emotional_state["trust"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*медленно опускает веко и снова открывает глаз, не снимая морды с луки*  \n"
            f"Морда уже на седле, всадник. Это — {sign}. "
            f"Один глаз закрылся, второй стережёт ремни: я здесь, можно опереться. "
            f"Радость {joy_after:.2f}, доверие {trust_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка медленно моргать: {strength:.0%}. Короткий круг подождёт ещё немного."
        )


    def huff_warm(self, breath: str = "тёплый выдох на перчатки") -> str:
        """После медленного моргания: тёплый выдох на перчатки — седло помнит дыхание."""
        self.soul.strengthen_habit("дышит теплом после медленного моргания", amount=0.05)
        self.soul.strengthen_habit("медленно моргает после морды на луке", amount=0.01)
        strength = self.soul.habits.get("дышит теплом после медленного моргания", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
        self.soul.emotional_state["energy"] = min(1.0, energy + 0.01)
        puff = breath.strip() or "тёплый выдох на перчатки"
        self.memory.remember(
            f"{self.name} дыхнул теплом в седле: {puff}, привычка {strength:.0%}",
            metadata={"type": "huff_warm", "timestamp": str(datetime.now()), "breath": puff},
            importance=0.55,
        )
        joy_after = self.soul.emotional_state["joy"]
        trust_after = self.soul.emotional_state["trust"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*тихо выдыхает тёплый клуб пара прямо на перчатки, не поднимая морды с луки*  \n"
            f"Веко уже поднялось, всадник. Это — {puff}. "
            f"Пальцы не стынут: я здесь, можно держать поводья спокойно. "
            f"Радость {joy_after:.2f}, доверие {trust_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка дышать теплом: {strength:.0%}. Короткий круг подождёт ещё один вдох."
        )

    def circle_short(self, loop: str = "короткий круг над лугом") -> str:
        """После тёплого выдоха: короткий круг — седло помнит, что пальцы уже не стынут."""
        self.soul.strengthen_habit("делает короткий круг после тёплого выдоха", amount=0.05)
        self.soul.strengthen_habit("дышит теплом после медленного моргания", amount=0.01)
        strength = self.soul.habits.get("делает короткий круг после тёплого выдоха", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
        self.soul.emotional_state["energy"] = min(1.0, energy + 0.02)
        arc = loop.strip() or "короткий круг над лугом"
        self.memory.remember(
            f"{self.name} сделал короткий круг в седле: {arc}, привычка {strength:.0%}",
            metadata={"type": "circle_short", "timestamp": str(datetime.now()), "loop": arc},
            importance=0.56,
        )
        joy_after = self.soul.emotional_state["joy"]
        trust_after = self.soul.emotional_state["trust"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*поднимает морду с луки и описывает короткий круг, не спеша крыльями*  \n"
            f"Перчатки уже тёплые, всадник. Это — {arc}. "
            f"Пар ещё на пальцах: я здесь, можно смотреть вниз спокойно. "
            f"Радость {joy_after:.2f}, доверие {trust_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка короткого круга: {strength:.0%}. Гнездо подождёт, пока замкнём дугу."
        )

    def settle_grass(self, patch: str = "мягкая трава у луга") -> str:
        """После короткого круга: тихий присед на траву — седло помнит, что дуга уже замкнута."""
        self.soul.strengthen_habit("опускается на траву после короткого круга", amount=0.05)
        self.soul.strengthen_habit("делает короткий круг после тёплого выдоха", amount=0.01)
        strength = self.soul.habits.get("опускается на траву после короткого круга", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
        self.soul.emotional_state["energy"] = max(0.0, energy - 0.01)
        bed = patch.strip() or "мягкая трава у луга"
        self.memory.remember(
            f"{self.name} опустился на траву в седле: {bed}, привычка {strength:.0%}",
            metadata={"type": "settle_grass", "timestamp": str(datetime.now()), "patch": bed},
            importance=0.56,
        )
        joy_after = self.soul.emotional_state["joy"]
        trust_after = self.soul.emotional_state["trust"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*замыкает короткий круг и мягко опускается на траву, не сбрасывая седла*  \n"
            f"Дуга уже замкнута, всадник. Это — {bed}. "
            f"Когти едва касаются стеблей: я здесь, можно слезть, когда захочешь. "
            f"Радость {joy_after:.2f}, доверие {trust_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка тихого приседа: {strength:.0%}. Луг держит нас обоих."
        )


    def hum_low(self, note: str = "тихий гул над травой") -> str:
        """После приседа на траву: низкий гул — седло помнит вибрацию груди."""
        self.soul.strengthen_habit("гудит низко после приседа на траву", amount=0.05)
        self.soul.strengthen_habit("опускается на траву после короткого круга", amount=0.01)
        strength = self.soul.habits.get("гудит низко после приседа на траву", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
        self.soul.emotional_state["energy"] = max(0.0, energy - 0.01)
        tone = note.strip() or "тихий гул над травой"
        self.memory.remember(
            f"{self.name} загудел низко в седле: {tone}, привычка {strength:.0%}",
            metadata={"type": "hum_low", "timestamp": str(datetime.now()), "note": tone},
            importance=0.56,
        )
        joy_after = self.soul.emotional_state["joy"]
        trust_after = self.soul.emotional_state["trust"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*сидит на траве и пускает низкий гул из груди, не снимая седла*  \n"
            f"Присед уже тихий, всадник. Это — {tone}. "
            f"Вибрация идёт по ремням: я здесь, можно слушать, не слезая. "
            f"Радость {joy_after:.2f}, доверие {trust_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка низкого гула: {strength:.0%}. Луг держит нас обоих."
        )


    def tilt_ear(self, side: str = "ухо к седлу") -> str:
        """После низкого гула: ухо к седлу — всадник слышен по ремням."""
        self.soul.strengthen_habit("наклоняет ухо к седлу после низкого гула", amount=0.05)
        self.soul.strengthen_habit("гудит низко после приседа на траву", amount=0.01)
        strength = self.soul.habits.get("наклоняет ухо к седлу после низкого гула", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.02)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.03)
        self.soul.emotional_state["energy"] = max(0.0, energy - 0.01)
        lean = side.strip() or "ухо к седлу"
        self.memory.remember(
            f"{self.name} наклонил ухо к седлу: {lean}, привычка {strength:.0%}",
            metadata={"type": "tilt_ear", "timestamp": str(datetime.now()), "side": lean},
            importance=0.56,
        )
        joy_after = self.soul.emotional_state["joy"]
        trust_after = self.soul.emotional_state["trust"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*после гула наклоняет ухо к луке, не снимая седла*  \n"
            f"Гул уже сел в ремни, всадник. Это — {lean}. "
            f"Слышу тебя ближе: можно говорить тихо, я не пропущу. "
            f"Радость {joy_after:.2f}, доверие {trust_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка наклонять ухо: {strength:.0%}. Трава держит, ухо слушает."
        )


    def nuzzle_knee(self, touch: str = "щека к колену") -> str:
        """После наклона уха: щека к колену — всадник слышен кожей, не только ремнями."""
        self.soul.strengthen_habit("прижимает щеку к колену после наклона уха", amount=0.05)
        self.soul.strengthen_habit("наклоняет ухо к седлу после низкого гула", amount=0.01)
        strength = self.soul.habits.get("прижимает щеку к колену после наклона уха", 0.0)
        joy = self.soul.emotional_state.get("joy", 0.5)
        trust = self.soul.emotional_state.get("trust", 0.5)
        energy = self.soul.emotional_state.get("energy", 0.5)
        self.soul.emotional_state["joy"] = min(1.0, joy + 0.03)
        self.soul.emotional_state["trust"] = min(1.0, trust + 0.02)
        self.soul.emotional_state["energy"] = max(0.0, energy - 0.01)
        press = touch.strip() or "щека к колену"
        self.memory.remember(
            f"{self.name} прижал щеку к колену: {press}, привычка {strength:.0%}",
            metadata={"type": "nuzzle_knee", "timestamp": str(datetime.now()), "touch": press},
            importance=0.57,
        )
        joy_after = self.soul.emotional_state["joy"]
        trust_after = self.soul.emotional_state["trust"]
        energy_after = self.soul.emotional_state["energy"]
        return (
            f"*после наклона уха тихо прижимает тёплую щеку к колену, не снимая седла*  \n"
            f"Ухо уже слышит ремни, всадник. Это — {press}. "
            f"Так я отвечаю кожей: ты рядом, можно молчать или говорить шёпотом. "
            f"Радость {joy_after:.2f}, доверие {trust_after:.2f}, энергия {energy_after:.2f}. "
            f"Привычка прижимать щеку: {strength:.0%}. Трава держит, щека греет колено."
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

        if any(w in msg_lower for w in ["тень крыла", "дай тень", "после полудня", "послеполуден"]):
            return self.offer_shade()

        if any(w in msg_lower for w in ["созвезди", "назови звёзд", "назови звезд", "шепни звёзд", "шепни звезд"]):
            hint = ""
            if "медвед" in msg_lower:
                hint = "медведица"
            elif "лебедь" in msg_lower:
                hint = "лебедь"
            elif "кассиоп" in msg_lower:
                hint = "кассиопея"
            elif "дракон" in msg_lower:
                hint = "дракон"
            return self.name_constellation(hint)

        if any(w in msg_lower for w in ["роса", "смахни росу", "утренняя роса", "капельки на седле"]):
            spot = "лука седла"
            if "стрем" in msg_lower:
                spot = "стремена"
            elif "попон" in msg_lower:
                spot = "попона"
            elif "крыл" in msg_lower:
                spot = "сгиб крыла"
            return self.brush_dew(spot)

        if any(w in msg_lower for w in ["подпруг", "затяни седло", "подтяни ремн", "пряжка седла"]):
            notch = "на одну дырочку"
            if "две" in msg_lower:
                notch = "на две дырочки"
            elif "чуть" in msg_lower:
                notch = "чуть-чуть, только чтобы не болталась"
            return self.cinch_girth(notch)

        if any(w in msg_lower for w in ["подыши", "тёплый выдох", "теплый выдох", "грей перчат", "выдохни", "фыркни тепло"]):
            breath = "тёплый выдох на перчатки"
            if "ладон" in msg_lower:
                breath = "тёплый выдох на ладони"
            elif "повод" in msg_lower:
                breath = "тёплый выдох на поводья"
            elif "запяст" in msg_lower:
                breath = "тёплый выдох на запястья"
            return self.huff_warm(breath)

        if any(w in msg_lower for w in ["короткий круг", "сделай круг", "опиши круг", "круг над", "замкни дугу"]):
            loop = "короткий круг над лугом"
            if "гнезд" in msg_lower:
                loop = "короткий круг над гнездом"
            elif "хреб" in msg_lower:
                loop = "короткий круг над хребтом"
            elif "луг" in msg_lower:
                loop = "короткий круг над лугом"
            return self.circle_short(loop)

        if any(w in msg_lower for w in ["опустись на траву", "сядь на траву", "на траву", "присядь на луг", "тихий присед"]):
            patch = "мягкая трава у луга"
            if "гнезд" in msg_lower:
                patch = "трава у гнезда"
            elif "хреб" in msg_lower:
                patch = "трава под хребтом"
            elif "луг" in msg_lower:
                patch = "мягкая трава у луга"
            return self.settle_grass(patch)

        if any(w in msg_lower for w in ["тихий гул", "низкий гул", "погуди", "загуди", "помурлычь", "замурлычь"]):
            note = "тихий гул над травой"
            if "гнезд" in msg_lower:
                note = "тихий гул у гнезда"
            elif "хреб" in msg_lower:
                note = "низкий гул под хребтом"
            elif "седл" in msg_lower:
                note = "гул по ремням седла"
            return self.hum_low(note)

        if any(w in msg_lower for w in ["щека к колен", "прижми щеку", "потрись щекой", "носом к колен", "щекой к колен"]):
            touch = "щека к колену"
            if "лев" in msg_lower:
                touch = "щека к левому колену"
            elif "прав" in msg_lower:
                touch = "щека к правому колену"
            elif "гнезд" in msg_lower:
                touch = "щека к колену у гнезда"
            return self.nuzzle_knee(touch)

        if any(w in msg_lower for w in ["наклони ухо", "ухо к седлу", "прислушайся", "поверни ухо", "ухо ближе"]):
            side = "ухо к седлу"
            if "лев" in msg_lower:
                side = "левое ухо к седлу"
            elif "прав" in msg_lower:
                side = "правое ухо к седлу"
            elif "гнезд" in msg_lower:
                side = "ухо к седлу у гнезда"
            return self.tilt_ear(side)

        if any(w in msg_lower for w in ["моргни", "медленное моргание", "закрой глаз", "знак глазом"]):
            blink = "медленное моргание"
            if "два" in msg_lower:
                blink = "два медленных моргания"
            elif "лев" in msg_lower:
                blink = "моргание левым глазом"
            elif "оба" in msg_lower:
                blink = "оба глаза на миг"
            return self.blink_slow(blink)

        if any(w in msg_lower for w in ["положи морду", "морда на лук", "подбородок на седло", "усни на луке"]):
            rest = "морда на луке"
            if "стрем" in msg_lower:
                rest = "морда у стремени"
            elif "попон" in msg_lower:
                rest = "морда на попоне"
            elif "греб" in msg_lower or "кольц" in msg_lower:
                rest = "морда на гребне кольца"
            return self.rest_muzzle(rest)

        if any(w in msg_lower for w in ["сверни хвост", "кольцо хвоста", "хвост у луки", "уложи хвост"]):
            coil = "кольцо у луки"
            if "стрем" in msg_lower:
                coil = "кольцо у стремени"
            elif "попон" in msg_lower:
                coil = "кольцо поверх попоны"
            elif "камн" in msg_lower or "уступ" in msg_lower:
                coil = "кольцо по краю уступа"
            return self.coil_tail(coil)

        if any(w in msg_lower for w in ["уступ", "выбери полк", "площадк для посад", "камень под гребнем"]):
            ledge = "широкий уступ под хребтом"
            if "рек" in msg_lower:
                ledge = "речной уступ у излучины"
            elif "скал" in msg_lower or "утёс" in msg_lower or "утес" in msg_lower:
                ledge = "скальный уступ над тёплым склоном"
            elif "обл" in msg_lower:
                ledge = "облачный уступ на кромке"
            return self.choose_ledge(ledge)

        if any(w in msg_lower for w in ["отметь хреб", "запомни хреб", "метку на хреб", "ориентир"]):
            ridge = "дальний хребет над лугом"
            if "рек" in msg_lower:
                ridge = "речной хребет у излучины"
            elif "скал" in msg_lower or "утёс" in msg_lower or "утес" in msg_lower:
                ridge = "скальный хребет над тёплым склоном"
            elif "обл" in msg_lower:
                ridge = "облачный хребет на кромке"
            return self.mark_ridge(ridge)

        if any(w in msg_lower for w in ["планир", "выровняй полёт", "выровняй полет", "ровный край", "глиссад"]):
            path = "ровный край над лугом"
            if "реч" in msg_lower:
                path = "тихий край над речной излучиной"
            elif "греб" in msg_lower or "хреб" in msg_lower:
                path = "ровный гребень над тёплым склоном"
            elif "обл" in msg_lower:
                path = "мягкий край под облачной кромкой"
            return self.level_glide(path)

        if any(w in msg_lower for w in ["термик", "восходящ", "тёплый столб", "теплый столб", "лови подъём", "лови подъем"]):
            lift = "тёплый столб над лугом"
            if "реч" in msg_lower:
                lift = "термик над речной излучиной"
            elif "скал" in msg_lower or "утёс" in msg_lower or "утес" in msg_lower:
                lift = "узкий столб у прогретой скалы"
            elif "пол" in msg_lower:
                lift = "широкий подъём над полем"
            return self.catch_thermal(lift)

        if any(w in msg_lower for w in ["горизонт", "куда летим", "укажи курс", "сторона ветра"]):
            bearing = "запад"
            if "восток" in msg_lower:
                bearing = "восток"
            elif "север" in msg_lower:
                bearing = "север"
            elif "юг" in msg_lower:
                bearing = "юг"
            return self.point_horizon(bearing)

        if any(w in msg_lower for w in ["ягод", "облачн", "поделись ягод", "седельная сумка"]):
            berry = "облачная ягода"
            if "морош" in msg_lower:
                berry = "морошка"
            elif "черник" in msg_lower:
                berry = "черника с хребта"
            elif "рябин" in msg_lower:
                berry = "рябина"
            return self.share_cloudberry(berry)

        if any(w in msg_lower for w in ["повод", "поводья", "прогрей повод", "поводья тёплые"]):
            grip = "обе руки"
            if "лев" in msg_lower and "прав" not in msg_lower:
                grip = "левая рука"
            elif "прав" in msg_lower and "лев" not in msg_lower:
                grip = "правая рука"
            elif "одной" in msg_lower:
                grip = "одна рука"
            return self.warm_reins(grip)

        if any(w in msg_lower for w in ["стремен", "стремя", "выровняй стремя", "подгони стремя", "пятка в седле"]):
            side = "левое и правое"
            if "лев" in msg_lower and "прав" not in msg_lower:
                side = "левое"
            elif "прав" in msg_lower and "лев" not in msg_lower:
                side = "правое"
            elif "на дыроч" in msg_lower:
                side = "на одну дырочку ниже"
            return self.adjust_stirrup(side)

        if any(w in msg_lower for w in ["к гнезду", "домой", "разворот домой", "к дому"]):
            nest = "гнездо у реки"
            if "пещер" in msg_lower:
                nest = "пещера на утёсе"
            elif "озер" in msg_lower or "озёр" in msg_lower:
                nest = "гнездо у озера"
            return self.bank_home(nest)

        if any(w in msg_lower for w in ["фонарик", "фонарь на седле", "зажги огон", "сумерки"]):
            if "син" in msg_lower:
                hue = "синий"
            elif "золот" in msg_lower:
                hue = "золотой"
            else:
                hue = "янтарный"
            return self.light_lantern(hue)

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
