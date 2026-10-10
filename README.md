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
- **Методы** `mood()`, `describe_soul()`, `habits()`, `soft_landing()`, `check_saddle()`, `fold_wings()`, `share_pebble()`, `pour_thermos()`, `offer_shade()`, `light_lantern()`, `name_constellation()`, `bank_home()`, `brush_dew()`, `cinch_girth()`, `adjust_stirrup()`, `warm_reins()`, `share_cloudberry()`, `point_horizon()`, `catch_thermal()`, `level_glide()`, `mark_ridge()`, `choose_ledge()`, `coil_tail()`, `rest_muzzle()`, `blink_slow()`, `huff_warm()`, `circle_short()`, `settle_grass()`, `hum_low()`, `tilt_ear()`, `nuzzle_knee()`, `purr_soft()`, `stretch_neck()`, `shake_leaves()`, `smooth_pommel()`, `share_apple()`, `wipe_juice()`, `dry_wing()`, `tuck_tip()`, `pin_tip()`, `cover_pin()`, `press_palm()`, `lift_palm()`, `trace_scale()`, `blot_scale()`, `fold_cloth()`, `shade_pommel()`, `ease_wing()`, `settle_stirrup()`, `snug_buckle()`, `tuck_strap()`, `warm_strap()`, `count_stitch()`, `name_thread()`, `tuck_thread()`, `glance_thread()`, `knot_thread()`, `huff_knot()`, `tap_knot()`, `listen_knot()`, `count_loops()`, `trace_loops()`, `name_loops()`, `shade_loops()`, `warm_loops()`, `drape_loops()`, `smooth_drape()`, `tuck_lantern()`, `tilt_glass()`, `share_crumb()`, `sweep_crumb()`, `rest_stripe()`, `shift_stripe()`, `curl_fingers()`, `ease_fold()`, `lay_warmth()`, `pat_pommel()`, `nuzzle_pommel()`, `stroke_pommel()`, `settle_pommel()`
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
python examples/saturday_morning_trace_scale.py   # ← НОВОЕ! обвести чешуйку после подъёма ладони
python examples/saturday_october_10_pat_pommel.py   # погладить луку утром 10 октября после тепла
python examples/saturday_october_10_nuzzle_pommel.py   # прижать морду к луке утром 10 октября после выдоха
python examples/saturday_afternoon_stroke_pommel.py   # ← НОВОЕ! гладить луку ладонью после полудня 10 октября
python examples/saturday_afternoon_settle_pommel.py   # ← НОВОЕ! опереться ладонью на луку после поглаживания 10 октября
python examples/friday_evening_lay_warmth.py   # тепло сгиба на луке к вечеру 9 октября
# ... (остальные примеры сохранены)
python examples/habits_demo.py
python examples/interactive_dragon.py
pytest tests/test_settle_pommel.py tests/test_stroke_pommel.py
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
- выравнивает стремена к полдню
- прогревает поводья после полудня
- делится облачной ягодой после поводьев
- указывает горизонт после ягоды
- ловит термик после горизонта
- выравнивает планирование после термика
- отмечает хребет после планирования
- выбирает уступ после хребта
- сворачивает хвост после уступа
- кладет морду на луку после хвоста
- медленно моргает после морды на луке
- дышит теплом после медленного моргания
- делает короткий круг после тёплого выдоха
- опускается на траву после короткого круга
- гудит низко после приседа на траву
- наклоняет ухо к седлу после низкого гула
- прижимает щеку к колену после наклона уха
- мурлычет в седло после щеки у колена
- тянет шею после тихого мурлыканья
- стряхивает кленовые листья после потяжки шеи
- разглаживает луку после кленовых листьев
- делится яблоком после гладкой луки
- вытирает сок с луки после яблока
- сушит край крыла после сока
- подгибает кончик крыла после сушки
- закрепляет кончик крыла после подгиба
- накрывает чешуйку после закрепления
- прижимает ладонь после накрытия
- поднимает ладонь после нажатия
- обводит чешуйку после подъёма ладони
- ставит седло под луну
- мягко садится перед выходными
- проверяет седло в полдень
- складывает крылья после полёта
- делится тёплым термосом в седле
- даёт тень крылом после полудня
- зажигает фонарик на седле к вечеру
- гладит луку ладонью после полудня
- опирается ладонью на луку после полудня

```python
dragon.soul.strengthen_habit("любит почесывания за ухом", 0.1)
dragon.soul.add_habit("всегда ждёт у окна", 0.4)
print(dragon.settle_pommel("луку после поглаживания"))
print(dragon.stroke_pommel("лука после полудня"))
```

Версия: 0.1.89
