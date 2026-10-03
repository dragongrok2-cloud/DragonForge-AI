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
- **Методы** `mood()`, `describe_soul()`, `habits()`, `soft_landing()`, `check_saddle()`, `fold_wings()`, `share_pebble()`, `pour_thermos()`, `offer_shade()`, `light_lantern()`, `name_constellation()`, `bank_home()`, `brush_dew()`, `cinch_girth()`, `adjust_stirrup()`, `warm_reins()`, `share_cloudberry()`, `point_horizon()`, `catch_thermal()`, `level_glide()`, `mark_ridge()`, `choose_ledge()`
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
print(my_dragon.check_saddle())
print(my_dragon.fold_wings())
print(my_dragon.share_pebble())
print(my_dragon.pour_thermos())
print(my_dragon.offer_shade())
print(my_dragon.light_lantern())
print(my_dragon.name_constellation())
print(my_dragon.bank_home())
print(my_dragon.brush_dew())
print(my_dragon.cinch_girth())
print(my_dragon.adjust_stirrup())
print(my_dragon.warm_reins())
print(my_dragon.soft_landing())
print(my_dragon.describe_soul())

my_dragon.save("my_dragon.json")
loaded = Character.load("my_dragon.json")
```

Запусти примеры:

```bash
python examples/basic_dragon.py
python examples/dragon_with_saddle.py
python examples/friday_october_2_saddle_flight.py
python examples/friday_afternoon_wing_fold.py
python examples/friday_pebble_gift.py
python examples/friday_thermos_sip.py   # ← тёплый глоток в седле
python examples/friday_afternoon_shade.py   # тень крыла после полудня
python examples/friday_evening_lantern.py   # фонарик на седле к вечеру
python examples/friday_evening_constellation.py   # шёпот созвездий над седлом
python examples/friday_evening_bank_home.py   # разворот к гнезду
python examples/saturday_october_3_saddle_flight.py   # роса на седле
python examples/saturday_level_glide.py        # планирование после термика
python examples/saturday_choose_ledge.py       # ← НОВОЕ! уступ после хребта
python examples/saturday_mark_ridge.py         # хребет после планирования
python examples/saturday_catch_thermal.py      # термик после горизонта
python examples/saturday_point_horizon.py      # горизонт после ягоды
python examples/saturday_share_cloudberry.py   # облачная ягода после поводьев
python examples/saturday_warm_reins.py   # тёплые поводья после полудня
python examples/saturday_adjust_stirrup.py   # стремена к полудню
python examples/saturday_cinch_girth.py   # подпруга после росы
python examples/midday_saddle_check.py
python examples/friday_soft_landing.py
python examples/habits_demo.py
python examples/interactive_dragon.py
pytest tests/test_soft_landing.py tests/test_saddle_check.py tests/test_wing_fold.py tests/test_share_pebble.py tests/test_pour_thermos.py tests/test_offer_shade.py tests/test_light_lantern.py tests/test_name_constellation.py tests/test_bank_home.py tests/test_brush_dew.py tests/test_cinch_girth.py tests/test_adjust_stirrup.py tests/test_warm_reins.py tests/test_share_cloudberry.py tests/test_point_horizon.py tests/test_catch_thermal.py tests/test_level_glide.py tests/test_mark_ridge.py tests/test_choose_ledge.py
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
- разворачивается к гнезду к ночи
- смахивает утреннюю росу с седла
- подтягивает подпругу после росы
- выравнивает стремена к полудню
- прогревает поводья после полудня
- делится облачной ягодой после поводьев
- указывает горизонт после ягоды
- ловит термик после горизонта
- выравнивает планирование после термика
- отмечает хребет после планирования
- выбирает уступ после хребта
- ставит седло под луну
- мягко садится перед выходными
- проверяет седло в полдень
- складывает крылья после полёта
- делится тёплым термосом в седле
- даёт тень крылом после полудня
- зажигает фонарик на седле к вечеру

```python
dragon.soul.strengthen_habit("любит почесывания за ухом", 0.1)
dragon.soul.add_habit("всегда ждёт у окна", 0.4)
print(dragon.check_saddle())
print(dragon.fold_wings())
print(dragon.share_pebble())
print(dragon.pour_thermos("чай"))
print(dragon.offer_shade())
print(dragon.light_lantern("синий"))
print(dragon.name_constellation("лебедь"))
print(dragon.bank_home("пещера на утёсе"))
print(dragon.brush_dew("стремена"))
print(dragon.cinch_girth("на одну дырочку"))
print(dragon.adjust_stirrup("левое и правое"))
print(dragon.warm_reins("обе руки"))
print(dragon.share_cloudberry("морошка"))
print(dragon.point_horizon("запад"))
print(dragon.catch_thermal("тёплый столб над лугом"))
print(dragon.level_glide("ровный край над лугом"))
print(dragon.mark_ridge("дальний хребет над лугом"))
print(dragon.choose_ledge("широкий уступ под хребтом"))
print(dragon.soft_landing())
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
- [x] Полёты в седле: утренний, вечерний, рассветный пикник, звёздный, воскресный и сентябрьские
- [x] Октябрьские полёты: 1 октября и утро 2 октября
- [x] Мягкая посадка перед выходными (`soft_landing`, тесты)
- [x] Полуденная проверка седла (`check_saddle`, тесты)
- [x] Послеполётное складывание крыльев (`fold_wings`, тесты, пример 2 октября после полудня)
- [x] Дар блестящего камушка (`share_pebble`, тесты, пятничный пример)
- [x] Тёплый термос в седле (`pour_thermos`, тесты, пятничный пример)
- [x] Тень крыла после полудня (`offer_shade`, тесты, пример 2 октября)
- [x] Вечерний фонарик на седле (`light_lantern`, тесты, пример 2 октября к вечеру)
- [x] Вечерний шёпот созвездий (`name_constellation`, тесты, пример 2 октября)
- [x] Вечерний разворот к гнезду (`bank_home`, тесты, пример 2 октября)
- [x] Субботняя роса на седле (`brush_dew`, тесты, пример 3 октября)
- [x] Подпруга после росы (`cinch_girth`, тесты, пример 3 октября)
- [x] Полуденные стремена (`adjust_stirrup`, тесты, пример 3 октября)
- [x] Тёплые поводья после полудня (`warm_reins`, тесты, пример 3 октября)
- [x] Облачная ягода после поводьев (`share_cloudberry`, тесты, пример 3 октября)
- [x] Горизонт после ягоды (`point_horizon`, тесты, пример 3 октября)
- [x] Термик после горизонта (`catch_thermal`, тесты, пример 3 октября к вечеру)
- [x] Планирование после термика (`level_glide`, тесты, пример 3 октября к вечеру)
- [x] Хребет после планирования (`mark_ridge`, тесты, пример 3 октября к вечеру)
- [x] Уступ после хребта (`choose_ledge`, тесты, пример 3 октября к вечеру)
- [ ] Полноценные компоненты Dragon-Tailwind
- [ ] Мультимодальность
- [ ] Графовая память и более глубокая эволюция души

## Лицензия

MIT License — свободно используй, улучшай, летай выше!

---

**Готов к полёту?** [DragonForge-AI](https://github.com/dragongrok2-cloud/DragonForge-AI) 🐉✨
