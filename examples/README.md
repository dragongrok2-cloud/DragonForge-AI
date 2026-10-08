# Примеры полётов в седле

После полудня 8 октября петли уже названы: Мёд, Шов и Седло. Край крыла кладём над ними тенью — не развязывая узелок и не снимая седла.

```bash
python examples/thursday_shade_loops.py
pytest tests/test_shade_loops.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.shade_loops("тень крыла на петлях медового узелка после полудня"))
print(dragon.talk("Затени петли узелка"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Тень петель — в `dragonforge/rituals/shade_loops.py`. Версия пакета: 0.1.67.

# Примеры полётов в седле

К раннему дню 8 октября петли уже обведены когтем. Даём им три тихих имени — Мёд, Шов и Седло — не развязывая узелок и не снимая седла.

```bash
python examples/thursday_name_loops.py
pytest tests/test_name_loops.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.name_loops("имена петель медового узелка к раннему дню"))
print(dragon.talk("Назови петли узелка"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Имена петель — в `dragonforge/rituals/name_loops.py`. Версия пакета: 0.1.66.

# Примеры полётов в седле

К полудню 8 октября петли уже сосчитаны. Когтем обводим их, не развязывая узелок и не снимая седла.

```bash
python examples/thursday_trace_loops.py
pytest tests/test_trace_loops.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.trace_loops("коготь по петлям медового узелка к полудню"))
print(dragon.talk("Обведи петли узелка"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Полуденный обвод петель — в `dragonforge/rituals/trace_loops.py`. Версия пакета: 0.1.65.

# Примеры полётов в седле

Утро 8 октября. Узелок переночевал на шве. Только прикладываем ухо, не развязывая и не снимая седла.

```bash
python examples/thursday_listen_knot.py
pytest tests/test_listen_knot.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.listen_knot("ухо к медовому узелку утром"))
print(dragon.talk("Послушай узелок за ночь"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Утро узелка — в `dragonforge/rituals/late_morning.py`. Версия пакета: 0.1.63.

# Примеры полётов в седле

К вечеру 7 октября узелок уже тёплый от дыхания. Только постукиваем по нему когтем, не развязывая и не снимая седла.

```bash
python examples/wednesday_tap_knot.py
pytest tests/test_tap_knot.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.tap_knot("коготь по тёплому узелку к вечеру"))
print(dragon.talk("Постучи по узелку, он на месте?"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Вечер нитки — в `dragonforge/rituals/late_morning.py`. Версия пакета: 0.1.62.

# Примеры полётов в седле

К позднему дню 7 октября узелок уже тихий. Согреваем его коротким дыханием, не развязывая и не снимая седла.

```bash
python examples/wednesday_huff_knot.py
pytest tests/test_huff_knot.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.huff_knot("дыхание на медовый узелок к позднему дню"))
print(dragon.talk("Подыши на узелок, чтобы не стыл"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Поздний день нитки — в `dragonforge/rituals/late_morning.py`. Версия пакета: 0.1.61.

# Примеры полётов в седле

Послеполуденный ритуал 7 октября: глянуть медовый хвостик в свете, не разворачивая подворот.

```bash
python examples/wednesday_glance_thread.py
pytest tests/test_glance_thread.py
```

```python
print(dragon.glance_thread("медовый хвостик в послеполуденном свете"))
```

## 7 октября, полдень — конец нитки

Полуденный ритуал: прижать конец нитки под уже названные стежки.

```bash
python examples/wednesday_tuck_thread.py
pytest tests/test_tuck_thread.py
```

```python
print(dragon.tuck_thread("конец нитки под стежками к полудню"))
```

## 7 октября, к позднему утру — цвет нитки

Стежки уже посчитаны на тёплой складке. К позднему утру называем цвет нитки, подворот не разворачиваем, седло не снимаем.

```bash
python examples/wednesday_name_thread.py
pytest tests/test_name_thread.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.name_thread("цвет нитки на стежках к позднему утру"))
print(dragon.talk("Назови цвет нитки на стежках"))
```

## 7 октября, утро — стежки

Складка уже поглажена. Считаем стежки когтем, подворот не разворачиваем.

```bash
python examples/wednesday_count_stitch.py
pytest tests/test_count_stitch.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.count_stitch("стежки на тёплой складке утром"))
print(dragon.talk("Посчитай стежки на складке"))
```

## 6 октября, вечером — тёплый ремень

Конец уже под пряжкой. Вечерний воздух стынет, и складка кожи может затвердеть — согреваем её коротким дыханием, седло не снимаем.

```bash
python examples/tuesday_warm_strap.py
pytest tests/test_warm_strap.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.warm_strap("подвёрнутый ремень к вечеру"))
print(dragon.talk("Согрей подвёрнутый ремень, чтобы не стыл"))
```

## 6 октября, к вечеру — конец ремня

Пряжка уже прижата и молчит. Свободный конец ремня ещё хлопает — подворачиваем его когтем под пряжку, седло не снимаем.

```bash
python examples/tuesday_tuck_strap.py
pytest tests/test_tuck_strap.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.tuck_strap("конец ремня после тихой пряжки"))
print(dragon.talk("Подогни конец ремня, чтобы не хлопал"))
```

## 6 октября, после полудня — пряжка

Стремя уже ровное после опущенного края. Ветер ещё звенит пряжкой — прижимаем её когтем, седло не снимаем.

```bash
python examples/tuesday_snug_buckle.py
pytest tests/test_snug_buckle.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.snug_buckle("пряжка после ровного стремени"))
print(dragon.talk("Прижми пряжку после стремени"))
```

## 6 октября, после полудня — стремя

Край крыла уже опущен после тени. Ветер качнул стремя — выравниваем когтем, седло не снимаем.

```bash
python examples/tuesday_settle_stirrup.py
pytest tests/test_settle_stirrup.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.settle_stirrup("стремя после опущенного края"))
print(dragon.talk("Выровняй стремя после края крыла"))
```

# Примеры полётов в седле

Короткие сцены, в которых привычка крепнет, а седло не снимают.

## 6 октября, после полудня

Тень над лукой уже подержана. Край крыла чуть опускаем, чтобы повеяло, седло не снимаем.

```bash
python examples/tuesday_ease_wing.py
pytest tests/test_ease_wing.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.ease_wing("край крыла после полуденной тени"))
print(dragon.talk("Опусти край крыла после тени"))
```

## 6 октября, полдень

Край попоны уже под лукой. Солнце садится на кожу — держим край крыла тенью, седло не снимаем.

```bash
python examples/tuesday_shade_pommel.py
pytest tests/test_shade_pommel.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.shade_pommel("тень крыла над лукой в полдень"))
print(dragon.talk("Придержи крыло тенью над лукой"))
```

## 6 октября, к полудню

Роса с чешуйки уже промокнута. Край попоны складываем под луку, чтобы ветер его не поднимал.

```bash
python examples/tuesday_fold_cloth.py
pytest tests/test_fold_cloth.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.fold_cloth("край попоны под лукой после росы"))
print(dragon.talk("Сложи край попоны после росы"))
```

## 6 октября, утро

Ладонь уже поднята с чешуйки. Капля росы ещё на крае — её промокаем крылом, перчатка не липнет.

```bash
python examples/tuesday_blot_scale.py
pytest tests/test_blot_scale.py
```

## 7 октября, утро

Ночное дыхание ещё держит складку ремня. Утром только поглаживаем её, подворот не разворачиваем.

```bash
python examples/wednesday_pat_fold.py
pytest tests/test_pat_fold.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.pat_fold("тёплая складка ремня утром"))
print(dragon.talk("Погладь тёплую складку утром"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Позднее утро — в `dragonforge/rituals/late_morning.py`. Версия пакета: 0.1.61.


## 7 октября, к позднему дню

Хвостик уже блестел в свете. К позднему дню только завязываем маленький узелок, подворот не разворачиваем.

```bash
python examples/wednesday_knot_thread.py
pytest tests/test_knot_thread.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.knot_thread("узелок на медовом хвостике к позднему дню"))
print(dragon.talk("Завяжи медовый узелок"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Поздний день нитки — в `dragonforge/rituals/late_morning.py`. Версия пакета: 0.1.61.
