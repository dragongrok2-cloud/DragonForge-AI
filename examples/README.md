# Примеры полётов в седле

Утром 9 октября фонарик уже лежит под разглаженным краем. Только согреваем ладони о стекло, не вытаскивая фонарик и не снимая седла.

```bash
python examples/friday_morning_cup_glow.py
pytest tests/test_cup_glow.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.cup_glow("ладони о стекло фонарика под краем попоны утром"))
print(dragon.talk("Согрей ладони о стекло фонарика"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Утренние ладони на стекло — в `dragonforge/rituals/cup_glow.py`. Версия пакета: 0.1.72.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до фонарика под краем попоны.

```bash
python examples/thursday_evening_tuck_lantern.py
python examples/thursday_evening_smooth_drape.py
python examples/thursday_drape_loops.py
python examples/thursday_warm_loops.py
python examples/thursday_shade_loops.py
python examples/thursday_name_loops.py
python examples/thursday_trace_loops.py
python examples/thursday_listen_knot.py
pytest tests/test_cup_glow.py tests/test_tuck_lantern.py tests/test_smooth_drape.py tests/test_drape_loops.py
```
