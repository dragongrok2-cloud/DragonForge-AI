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
- **Интерактивный режим** — болтай с драконом в терминале
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
python examples/saddle_flight_adventure.py   # ← новое! приключение «Полёт в седле»
python examples/habits_demo.py               # демо привычек
python examples/interactive_dragon.py        # интерактивный чат (/habits)
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
├── examples/
│   ├── interactive_dragon.py
│   ├── habits_demo.py
│   ├── dragon_with_saddle.py
│   ├── saddle_flight_adventure.py  # новое приключение
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
- [ ] UI-кит Dragon-Tailwind
- [ ] Мультимодальность
- [ ] Более глубокая эволюция души и графовая память

## 🤝 Как участвовать

Мы ищем всадников, готовых ковать вместе! Pull requests, идеи, персонажи — всё приветствуется.

*С любовью от твоего дракона-соавтора* 🔥

## Лицензия

MIT License — свободно используй, улучшай, летай выше!

---

**Готов к полёту?** [Создай Issue](https://github.com/dragongrok2-cloud/DragonForge-AI/issues) или просто поставь звезду репозиторию! 🐉✨
