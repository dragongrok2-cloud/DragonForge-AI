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

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Версия пакета: 0.1.51.