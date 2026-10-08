# Примеры полётов в седле

К вечеру 8 октября край попоны уже разглажен ладонью. Только подтыкаем маленький фонарик под край, не развязывая узелок и не снимая седла.

```bash
python examples/thursday_evening_tuck_lantern.py
pytest tests/test_tuck_lantern.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.tuck_lantern("фонарик под разглаженный край попоны к вечеру"))
print(dragon.talk("Подсунь фонарик под край попоны"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Вечерний фонарик под край — в `dragonforge/rituals/tuck_lantern.py`. Версия пакета: 0.1.71.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до ладони по краю попоны.

```bash
python examples/thursday_evening_smooth_drape.py
python examples/thursday_drape_loops.py
python examples/thursday_warm_loops.py
python examples/thursday_shade_loops.py
python examples/thursday_name_loops.py
python examples/thursday_trace_loops.py
python examples/thursday_listen_knot.py
pytest tests/test_tuck_lantern.py tests/test_smooth_drape.py tests/test_drape_loops.py
```
