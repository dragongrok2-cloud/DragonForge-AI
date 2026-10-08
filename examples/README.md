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
