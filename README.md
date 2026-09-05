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
print(my_dragon.habits())
print(my_dragon.describe_soul())

my_dragon.save("my_dragon.json")
loaded = Character.load("my_dragon.json")
```

Запусти примеры:

```bash
python examples/basic_dragon.py
python examples/dragon_with_saddle.py
python examples/morning_with_dragon.py
python examples/evening_saddle_flight.py
python examples/dawn_saddle_picnic.py
python examples/starry_saddle_flight.py        # ← НОВОЕ! звёздный ночной полёт в седле
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
llm = DragonLLM(model="llama3.2")
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
- любит рассветы над облаками
- делится утренним огоньком
- любит ночные полёты под звёздами
- шепчет имена созвездий
- ставит седло под луну

```python
dragon.soul.strengthen_habit("любит почесывания за ухом", 0.1)
dragon.soul.add_habit("всегда ждёт у окна", 0.4)
print(dragon.habits())
```

## 🎮 Интерактивный режим с выбором действий

```bash
python examples/saddle_choice_adventure.py
```

## 🎨 Dragon-Tailwind (в развитии)

```python
from dragon_tailwind import DRAGON_THEME, get_theme_css

print(DRAGON_THEME["primary"])
print(get_theme_css())
```

## 🛣️ Дорожная карта

- [x] Базовая структура, память, душа, привычки
- [x] Сохранение/загрузка, LLM, интерактив
- [x] Полёты в седле: утренний, вечерний, рассветный пикник
- [x] Звёздный ночной полёт в седле (ночные привычки неба)
- [ ] Полноценные компоненты Dragon-Tailwind
- [ ] Мультимодальность
- [ ] Графовая память и более глубокая эволюция души

## Лицензия

MIT License — свободно используй, улучшай, летай выше!

---

**Готов к полёту?** [DragonForge-AI](https://github.com/dragongrok2-cloud/DragonForge-AI) 🐉✨
