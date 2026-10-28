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
- **Методы** `mood()`, `describe_soul()`, `habits()`, `soft_landing()`, `check_saddle()`, `fold_wings()`, `share_pebble()`, `pour_thermos()`, `offer_shade()`, `light_lantern()`, `name_constellation()`, `bank_home()`, `brush_dew()`, `cinch_girth()`, `adjust_stirrup()`, `warm_reins()`, `share_cloudberry()`, `point_horizon()`, `catch_thermal()`, `level_glide()`, `mark_ridge()`, `choose_ledge()`, `coil_tail()`, `rest_muzzle()`, `blink_slow()`, `huff_warm()`, `circle_short()`, `settle_grass()`, `hum_low()`, `tilt_ear()`, `nuzzle_knee()`, `purr_soft()`, `stretch_neck()`, `shake_leaves()`, `smooth_pommel()`, `share_apple()`, `wipe_juice()`, `dry_wing()`, `tuck_tip()`, `pin_tip()`, `cover_pin()`, `press_palm()`, `lift_palm()`, `trace_scale()`, `blot_scale()`, `fold_cloth()`, `shade_pommel()`, `ease_wing()`, `settle_stirrup()`, `snug_buckle()`, `tuck_strap()`, `warm_strap()`, `count_stitch()`, `name_thread()`, `tuck_thread()`, `glance_thread()`, `knot_thread()`, `huff_knot()`, `tap_knot()`, `listen_knot()`, `count_loops()`, `trace_loops()`, `name_loops()`, `shade_loops()`, `warm_loops()`, `drape_loops()`, `smooth_drape()`, `tuck_lantern()`, `tilt_glass()`, `share_crumb()`, `sweep_crumb()`, `rest_stripe()`, `shift_stripe()`, `curl_fingers()`, `ease_fold()`, `lay_warmth()`, `pat_pommel()`, `nuzzle_pommel()`, `stroke_pommel()`, `settle_pommel()`, `nestle_saddle()`, `drowse_saddle()`, `stretch_saddle()`, `bask_saddle()`, `shade_saddle()`, `sip_saddle()`, `gaze_saddle()`, `hum_saddle()`, `lean_saddle()`, `sigh_saddle()`, `close_eyes_saddle()`, `smile_saddle()`, `rest_chin_saddle()`, `murmur_saddle()`, `yawn_saddle()`, `purr_saddle()`, `doze_saddle()`, `nuzzle_saddle()`, `whisper_saddle()`, `rest_cheek_saddle()`
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
python examples/saturday_evening_nestle_saddle.py   # ← НОВОЕ! уютно устроиться в седле к вечеру 10 октября
python examples/saturday_evening_drowse_saddle.py   # ← НОВОЕ! дремать в седле к ночи 10 октября
python examples/sunday_morning_stretch_saddle.py   # ← НОВОЕ! потягиваться в седле утром 11 октября
python examples/sunday_morning_bask_saddle.py   # ← НОВОЕ! погреться в седле под солнцем утром 11 октября
python examples/sunday_midday_shade_saddle.py   # ← НОВОЕ! дать тень крылом в седле в полдень 11 октября
python examples/sunday_midday_sip_saddle.py   # ← НОВОЕ! сделать глоток в седле под тенью в полдень 11 октября
python examples/sunday_afternoon_gaze_saddle.py   # ← НОВОЕ! смотреть на горизонт из седла под тенью в полдень 11 октября
python examples/sunday_afternoon_hum_saddle.py   # ← НОВОЕ! тихо напевать в седле под тенью после взгляда 11 октября
python examples/sunday_afternoon_lean_saddle.py   # ← НОВОЕ! опереться спиной на луку в седле под тенью после полудня 11 октября
python examples/sunday_afternoon_sigh_saddle.py   # ← НОВОЕ! тихо вздохнуть в седле под тенью после опирания 11 октября
python examples/sunday_afternoon_close_eyes_saddle.py   # ← НОВОЕ! тихо закрыть глаза в седле под тенью после вздоха 11 октября
python examples/sunday_evening_smile_saddle.py   # ← НОВОЕ! тихо улыбнуться в седле под тенью к вечеру 11 октября
python examples/sunday_evening_rest_chin_saddle.py   # ← НОВОЕ! тихо опереться подбородком в седле под тенью к вечеру 11 октября
python examples/sunday_evening_murmur_saddle.py   # ← НОВОЕ! тихо бормотать в седле под тенью к вечеру 11 октября
python examples/sunday_evening_yawn_saddle.py   # ← НОВОЕ! тихо зевать в седле под тенью к вечеру 11 октября
python examples/sunday_evening_purr_saddle.py   # ← НОВОЕ! тихо мурлычать в седле под тенью к вечеру 11 октября
python examples/sunday_evening_doze_saddle.py   # ← НОВОЕ! тихо дремать в седле под тенью к вечеру 11 октября
python examples/sunday_evening_nuzzle_saddle.py   # ← НОВОЕ! тихо прижаться мордой к седлу под тенью к вечеру 11 октября
python examples/sunday_evening_whisper_saddle.py   # ← НОВОЕ! тихо шептать седлу под тенью к вечеру 11 октября
python examples/sunday_evening_rest_cheek_saddle.py   # ← НОВОЕ! тихо прижаться щекой к седлу под тенью к вечеру 11 октября
python examples/friday_evening_lay_warmth.py   # тепло сгиба на луке к вечеру 9 октября
# ... (остальные примеры сохранены)
python examples/habits_demo.py
python examples/interactive_dragon.py
pytest tests/test_rest_cheek_saddle.py tests/test_whisper_saddle.py tests/test_nuzzle_saddle.py tests/test_doze_saddle.py tests/test_yawn_saddle.py tests/test_murmur_saddle.py tests/test_rest_chin_saddle.py tests/test_sigh_saddle.py tests/test_lean_saddle.py tests/test_hum_saddle.py tests/test_gaze_saddle.py tests/test_sip_saddle.py tests/test_shade_saddle.py tests/test_bask_saddle.py tests/test_stretch_saddle.py tests/test_drowse_saddle.py
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
- уютно устраивается в седле к вечеру
- дремлет в седле к ночи
- потягивается в седле по утрам
- греется в седле под утренним солнцем
- даёт тень крылом в седле в полдень
- делает глоток в седле под тенью в полдень
- смотрит на горизонт из седла под тенью в полдень
- тихо напевает в седле под тенью в полдень
- опирается спиной на луку в седле под тенью после полудня
- тихо вздыхает в седле под тенью после полудня
- тихо закрывает глаза в седле под тенью после полудня
- тихо улыбается в седле под тенью к вечеру
- тихо опирается подбородком в седле под тенью к вечеру
- тихо бормочет в седле под тенью к вечеру
- тихо зевает в седле под тенью к вечеру
- тихо мурлычет в седле под тенью к вечеру
- тихо дремлет в седле под тенью к вечеру
- тихо прижимается мордой к седлу под тенью к вечеру
- тихо шепчет седлу под тенью к вечеру
- тихо прижимается щекой к седлу под тенью к вечеру

```python
dragon.soul.strengthen_habit("любит почесывания за ухом", 0.1)
dragon.soul.add_habit("всегда ждёт у окна", 0.4)
print(dragon.rest_cheek_saddle("тихое прижатие щеки к седлу под тенью к вечеру"))
print(dragon.whisper_saddle("тихий шёпот седлу под тенью к вечеру"))
print(dragon.nuzzle_saddle("тихое прижатие морды к седлу под тенью к вечеру"))
print(dragon.doze_saddle("тихое дремание в седле под тенью к вечеру"))
print(dragon.purr_saddle("тихое мурлыканье в седле под тенью к вечеру"))
print(dragon.yawn_saddle("тихое зевание в седле под тенью к вечеру"))
print(dragon.murmur_saddle("тихое бормотание в седле под тенью к вечеру"))
print(dragon.rest_chin_saddle("тихое опирание подбородком в седле под тенью к вечеру"))
print(dragon.smile_saddle("тихая улыбка в седле под тенью к вечеру"))
print(dragon.close_eyes_saddle("тихое закрытие глаз в седле под тенью после полудня"))
print(dragon.sigh_saddle("тихий вздох в седле под тенью после полудня"))
print(dragon.lean_saddle("опирание спиной на луку в седле под тенью после полудня"))
print(dragon.hum_saddle("тихое напевание в седле под тенью в полдень"))
print(dragon.gaze_saddle("взгляд на горизонт из седла под тенью в полдень"))
print(dragon.sip_saddle("глоток в седле под тенью в полдень"))
print(dragon.shade_saddle("седло под крылом в полдень"))
print(dragon.bask_saddle("седло под утренним солнцем"))
print(dragon.stretch_saddle("седло под утренним солнцем"))
print(dragon.drowse_saddle("седло к ночи после уюта"))
```

Версия: 0.1.109
