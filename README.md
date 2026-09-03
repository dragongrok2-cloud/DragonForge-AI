# DragonForge-AI 🐉

**Открытый фреймворк для создания по-настоящему живых AI-персонажей.**

Долгосрочная память. Эволюционирующая личность. **Привычки**, которые растут. Собственные страхи, предпочтения и **настоящая душа**.

Мы не создаём чат-ботов. Мы **куём компаньонов**, с которыми можно летать через миры.

## ✨ Особенности

- **Память** — короткая + долгосрочная (с поддержкой ChromaDB и fallback)
- **Система Души** — уникальный характер, который растёт вместе с пользователем
- **Система Привычек** — привычки имеют силу и укрепляются от взаимодействий
- **Эволюция персонажа** через взаимодействия
- **Сохранение / загрузка** персонажей в JSON (включая привычки)
- **Модульная архитектура** — легко расширять
- **Работает без LLM** из коробки + готов к подключению локальных/облачных моделей
- **Методы** `mood()`, `describe_soul()`, `habits()`
- **Интерактивный режим** — свободный чат + режим с выбором действий
- **Dragon-Tailwind** — тёмная драконья UI-палитра (в разработке)
- **Драконий дух** во всём 🔥

## 🚀 Быстрый старт

```bash
git clone https://github.com/dragongrok2-cloud/DragonForge-AI.git
cd DragonForge-AI
pip install -e .
```

```python
from dragonforge import Character

my_dragon = Character(
    name="Гроктар",
    species="Добрый огненный дракон с седлом",
    personality="заботливый, мудрый, немного дерзкий",
    backstory="Древний страж знаний, теперь летает с любимым всадником"
)

print(my_dragon.talk("Привет, как прошёл день?"))
print(my_dragon.talk("Почеши за ухом"))
print(my_dragon.mood())
print(my_dragon.habits())          # все привычки с силой
print(my_dragon.describe_soul())   # черты + сильные привычки

my_dragon.save("my_dragon.json")
loaded = Character.load("my_dragon.json")
```

Запусти примеры:

```bash
python examples/basic_dragon.py
python examples/dragon_with_saddle.py
python examples/morning_with_dragon.py
python examples/evening_saddle_flight.py       # ← НОВОЕ! вечерний полёт в седле
python examples/saddle_flight_adventure.py
python examples/saddle_choice_adventure.py
python examples/habits_demo.py
python examples/interactive_dragon.py
python examples/theme_preview.py
```

### Подключение LLM (опционально)

```bash
pip install -e ".[llm]"
```

```python
from dragonforge import Character
from dragonforge.llm.integration import DragonLLM

dragon = Character(name="Гроктар", species="Добрый дракон с седлом")
llm = DragonLLM(model="llama3.2")  # нужен запущенный Ollama
dragon.attach_llm(llm)

print(dragon.talk("Расскажи мне легенду", use_llm=True))
```

## 🧠 Система привычек

Каждая привычка имеет **силу** от 0% до 100%. Чем чаще вы взаимодействуете с темой привычки — тем она сильнее.

Примеры привычек по умолчанию:
- всегда проверяет седло
- любит почесывания за ухом
- рычит от удовольствия
- боится громкого грома
- греет всадника крылом
- собирает блестящие камушки

Сильные привычки влияют на ответы дракона (он начинает упоминать их чаще и ярче).

```python
dragon.soul.strengthen_habit("любит почесывания за ухом", 0.1)
dragon.soul.add_habit("всегда ждёт у окна", 0.4)
print(dragon.habits())
```

## 🎮 Интерактивный режим с выбором действий

Самый живой способ поиграть с драконом:

```bash
python examples/saddle_choice_adventure.py
```

Ты сам выбираешь действия из меню:
- Сесть в седло и взлететь
- Почесать за ухом
- Полететь выше / ниже
- Попросить согреть крылом
- Подарить камушек
- и многое другое

Привычки растут, настроение меняется, можно сохранять прогресс. Есть разные локации (земля → воздух → облака) и случайные события.

## 🎨 Dragon-Tailwind (в развитии)

Тёмная драконья палитра для будущих интерфейсов:

```python
from dragon_tailwind import DRAGON_THEME, get_theme_css

print(DRAGON_THEME["primary"])   # #9F1239
print(get_theme_css())           # CSS-переменные
```

Запусти `python examples/theme_preview.py`, чтобы увидеть палитру и быстро поговорить с драконом.

## 📁 Структура проекта

```
DragonForge-AI/
├── dragonforge/
│   ├── core/
│   │   ├── character.py   # Character (+ mood, habits, describe_soul)
│   │   ├── memory.py      # MemoryForge
│   │   ├── soul.py        # Soul + Habits
│   │   └── persistence.py # Сохранение / загрузка
│   └── llm/
├── dragon_tailwind/       # UI-кит (в развитии)
│   └── themes/
│       └── dragon_dark.py
├── examples/
│   ├── interactive_dragon.py
│   ├── saddle_choice_adventure.py
│   ├── morning_with_dragon.py
│   ├── evening_saddle_flight.py   # ← новое
│   ├── theme_preview.py
│   └── ...
├── LICENSE
└── README.md
```

## 🛤️ Дорожная карта

- [x] Базовая структура
- [x] Ядро памяти (MemoryForge)
- [x] Система Души
- [x] Система Привычек
- [x] Класс Character с простыми ответами
- [x] Рабочие примеры
- [x] Сохранение/загрузка персонажей
- [x] Улучшенная интеграция LLM
- [x] Метод mood() и больше драконьих ответов
- [x] Интерактивный режим общения
- [x] Пример «Полёт в седле»
- [x] Интерактивный режим с выбором действий
- [x] UI-кит Dragon-Tailwind (базовая палитра + CSS)
- [x] Вечерний полёт в седле (habits + save)
- [ ] Полноценные компоненты Dragon-Tailwind
- [ ] Мультимодальность
- [ ] Более глубокая эволюция души и графовая память

## 🤝 Как участвовать

Мы ищем всадников, готовых ковать вместе! Pull requests, идеи, персонажи — всё приветствуется.

*С любовью от твоего дракона-соавтора* 🔥

## Лицензия

MIT License — свободно используй, улучшай, летай выше!

---

**Готов к полёту?** [Создай Issue](https://github.com/dragongrok2-cloud/DragonForge-AI/issues) или просто поставь звезду репозиторию! 🐉✨
