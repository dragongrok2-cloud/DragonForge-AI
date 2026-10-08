# Примеры полётов в седле

К вечеру 8 октября край попоны уже лежит на согретых петлях. Только ведём ладонь по краю, не развязывая узелок и не снимая седла.

```bash
python examples/thursday_evening_smooth_drape.py
pytest tests/test_smooth_drape.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.smooth_drape("край попоны на петлях медового узелка к вечеру"))
print(dragon.talk("Погладь край попоны"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Вечерняя ладонь — в `dragonforge/rituals/smooth_drape.py`. Версия пакета: 0.1.70.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до края попоны к середине дня.

```bash
python examples/thursday_drape_loops.py
python examples/thursday_warm_loops.py
python examples/thursday_shade_loops.py
python examples/thursday_name_loops.py
python examples/thursday_trace_loops.py
python examples/thursday_listen_knot.py
pytest tests/test_smooth_drape.py tests/test_drape_loops.py tests/test_warm_loops.py
```
