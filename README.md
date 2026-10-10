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
- **Методы** `mood()`, `describe_soul()`, `habits()`, `soft_landing()`, `check_saddle()`, `fold_wings()`, `share_pebble()`, `pour_thermos()`, `offer_shade()`, `light_lantern()`, `name_constellation()`, `bank_home()`, `brush_dew()`, `cinch_girth()`, `adjust_stirrup()`, `warm_reins()`, `share_cloudberry()`, `point_horizon()`, `catch_thermal()`, `level_glide()`, `mark_ridge()`, `choose_ledge()`, `coil_tail()`, `rest_muzzle()`, `blink_slow()`, `huff_warm()`, `circle_short()`, `settle_grass()`, `hum_low()`, `tilt_ear()`, `nuzzle_knee()`, `purr_soft()`, `stretch_neck()`, `shake_leaves()`, `smooth_pommel()`, `share_apple()`, `wipe_juice()`, `dry_wing()`, `tuck_tip()`, `pin_tip()`, `cover_pin()`, `press_palm()`, `lift_palm()`, `trace_scale()`, `blot_scale()`, `fold_cloth()`, `shade_pommel()`, `ease_wing()`, `settle_stirrup()`, `snug_buckle()`, `tuck_strap()`, `warm_strap()`, `count_stitch()`, `name_thread()`, `tuck_thread()`, `glance_thread()`, `knot_thread()`, `huff_knot()`, `tap_knot()`, `listen_knot()`, `count_loops()`, `trace_loops()`, `name_loops()`, `shade_loops()`, `warm_loops()`, `drape_loops()`, `smooth_drape()`, `tuck_lantern()`, `tilt_glass()`, `share_crumb()`, `sweep_crumb()`, `rest_stripe()`, `shift_stripe()`, `curl_fingers()`, `ease_fold()`, `lay_warmth()`, `pat_pommel()`, `nuzzle_pommel()`
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
python examples/friday_evening_lay_warmth.py   # тепло сгиба на луке к вечеру 9 октября
python examples/friday_evening_ease_fold.py   # сгиб полоски солнца к вечеру 9 октября
python examples/friday_afternoon_curl_fingers.py   # пальцы в полоске солнца после полудня 9 октября
python examples/friday_afternoon_shift_stripe.py   # полоска солнца на костяшках после полудня 9 октября
python examples/friday_afternoon_rest_stripe.py   # ладонь на светлой полоске после полудня 9 октября
python examples/friday_afternoon_sweep_crumb.py   # крошка с полоски солнца после полудня 9 октября
python examples/friday_noon_share_crumb.py   # яблочная крошка на полоске солнца в полдень 9 октября
python examples/friday_eleven_tilt_glass.py   # полоска солнца на сухом стекле к одиннадцати
python examples/thursday_evening_tuck_lantern.py   # фонарик под разглаженный край попоны к вечеру
python examples/thursday_evening_smooth_drape.py   # ладонь по краю попоны к вечеру
python examples/thursday_drape_loops.py            # край попоны на согретых петлях к середине дня
python examples/thursday_shade_loops.py        # тень крыла на названных петлях после полудня
python examples/thursday_name_loops.py         # имена петель медового узелка к раннему дню
python examples/thursday_listen_knot.py        # ухо к медовому узелку утром
python examples/wednesday_tap_knot.py          # коготь по тёплому узелку к вечеру
python examples/wednesday_huff_knot.py         # дыхание на медовый узелок к позднему дню
python examples/wednesday_knot_thread.py        # узелок на медовом хвостике к позднему дню
python examples/wednesday_glance_thread.py      # медовый хвостик в послеполуденном свете
python examples/wednesday_tuck_thread.py        # конец нитки к полудню
python examples/wednesday_name_thread.py         # цвет нитки к позднему утру
python examples/tuesday_warm_strap.py          # ← НОВОЕ! тёплый ремень после подворота
python examples/tuesday_tuck_strap.py           # конец ремня после тихой пряжки
python examples/tuesday_snug_buckle.py          # пряжка после ровного стремени
python examples/tuesday_settle_stirrup.py        # стремя после опущенного края
python examples/tuesday_ease_wing.py             # край крыла после полуденной тени
python examples/tuesday_lift_palm.py             # ладонь с чешуйки утром после нажатия
python examples/monday_press_palm.py             # ладонь один раз после накрытия
python examples/monday_cover_pin.py              # ладонь на чешуйке после закрепления
python examples/monday_pin_tip.py                # кончик у луки после подгиба
python examples/monday_tuck_tip.py               # кончик крыла после сушки
python examples/monday_dry_wing.py               # край крыла после сока
python examples/monday_wipe_juice.py             # сок с луки после яблока
python examples/monday_share_apple.py            # яблоко после луки
python examples/monday_smooth_pommel.py          # лука после листьев
python examples/monday_shake_leaves.py           # кленовые листья с седла
python examples/monday_stretch_neck.py           # потяжка шеи после мурлыканья
python examples/sunday_purr_soft.py            # мурлыканье в седло после щеки
python examples/sunday_nuzzle_knee.py          # щека к колену после уха
python examples/sunday_tilt_ear.py             # ухо к седлу после гула
python examples/sunday_hum_low.py              # низкий гул после приседа
python examples/sunday_settle_grass.py         # тихий присед после круга
python examples/sunday_circle_short.py         # короткий круг после выдоха
python examples/sunday_huff_warm.py            # тёплый выдох после моргания
python examples/sunday_blink_slow.py           # медленное моргание после морды
python examples/sunday_rest_muzzle.py          # морда на луке после хвоста
python examples/sunday_coil_tail.py            # хвост после уступа
python examples/saturday_choose_ledge.py       # уступ после хребта
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
pytest tests/test_soft_landing.py tests/test_saddle_check.py tests/test_wing_fold.py tests/test_share_pebble.py tests/test_pour_thermos.py tests/test_offer_shade.py tests/test_light_lantern.py tests/test_name_constellation.py tests/test_bank_home.py tests/test_brush_dew.py tests/test_cinch_girth.py tests/test_adjust_stirrup.py tests/test_warm_reins.py tests/test_share_cloudberry.py tests/test_point_horizon.py tests/test_catch_thermal.py tests/test_level_glide.py tests/test_mark_ridge.py tests/test_choose_ledge.py tests/test_coil_tail.py tests/test_rest_muzzle.py tests/test_blink_slow.py tests/test_huff_warm.py tests/test_circle_short.py tests/test_settle_grass.py tests/test_hum_low.py tests/test_tilt_ear.py tests/test_nuzzle_knee.py tests/test_purr_soft.py tests/test_stretch_neck.py tests/test_shake_leaves.py tests/test_smooth_pommel.py tests/test_share_apple.py tests/test_wipe_juice.py tests/test_dry_wing.py tests/test_tuck_tip.py tests/test_pin_tip.py tests/test_cover_pin.py tests/test_press_palm.py tests/test_lift_palm.py tests/test_trace_scale.py
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
- стряхивает кленовые листья после потяжки шеи
- разглаживает луку после кленовых листьев
- прижимает ладонь после накрытия
- прижимает пряжку после ровного стремени
- подворачивает конец ремня после тихой пряжки
- согревает медовый узелок к позднему дню
- постукивает по тёплому узелку к вечеру
- слушает медовый узелок утром
- накрывает петли медового узелка тенью после полудня
- согревает названные петли дыханием к позднему дню
- накрывает согретые петли краем попоны к середине дня
- гладит край попоны на согретых петлях к вечеру
- подтыкает фонарик под разглаженный край попоны к вечеру
- наклоняет сухое стекло фонарика к одиннадцати
- делится яблочной крошкой на полоске солнца в полдень
- смахивает крошку с полоски солнца после полудня
- держит ладонь на светлой полоске после полудня
- сдвигает полоску солнца на костяшки после полудня
- сгибает пальцы в полоске солнца после полудня
- разжимает сгиб полоски солнца к вечеру
- кладёт тепло сгиба на луку к вечеру
- гладит луку утром после тепла
- прижимает морду к луке после тёплого выдоха

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
print(dragon.coil_tail("кольцо у луки"))
print(dragon.rest_muzzle("морда на луке"))
print(dragon.blink_slow("медленное моргание"))
print(dragon.huff_warm("тёплый выдох на перчатки"))
print(dragon.circle_short("короткий круг над лугом"))
print(dragon.settle_grass("мягкая трава у луга"))
print(dragon.hum_low("тихий гул над травой"))
print(dragon.tilt_ear("ухо к седлу"))
print(dragon.nuzzle_knee("щека к колену"))
print(dragon.purr_soft("тихое мурлыканье в седло"))
print(dragon.stretch_neck("тихая потяжка шеи над седлом"))
print(dragon.shake_leaves("кленовый лист с луки"))
print(dragon.smooth_pommel("лука после листьев"))
print(dragon.share_apple("кислое яблоко из седельной сумки"))
print(dragon.wipe_juice("сок с луки после яблока"))
print(dragon.dry_wing("край крыла после сока"))
print(dragon.tuck_tip("кончик крыла после сушки"))
print(dragon.pin_tip("кончик у луки после подгиба"))
print(dragon.cover_pin("ладонь на чешуйке после закрепления"))
print(dragon.press_palm("мягкое нажатие после накрытия"))
print(dragon.lift_palm("ладонь после ночного нажатия"))
print(dragon.trace_scale("чешуйка после подъёма ладони"))
```