# Примеры полётов в седле

К середине утра 9 октября ладони уже согрели стекло. Только промокаем бусинку росы краем крыла, не вытаскивая фонарик и не снимая седла.

```bash
python examples/friday_midmorning_blot_bead.py
pytest tests/test_blot_bead.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.blot_bead("бусинка росы со стекла фонарика к середине утра"))
print(dragon.talk("Промокни бусинку росы со стекла"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Бусинка росы со стекла — в `dragonforge/rituals/blot_bead.py`. Версия пакета: 0.1.73.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до ладоней на стекле.

```bash
python examples/friday_morning_cup_glow.py
python examples/thursday_evening_tuck_lantern.py
python examples/thursday_evening_smooth_drape.py
python examples/thursday_drape_loops.py
python examples/thursday_warm_loops.py
python examples/thursday_shade_loops.py
python examples/thursday_name_loops.py
python examples/thursday_trace_loops.py
python examples/thursday_listen_knot.py
pytest tests/test_blot_bead.py tests/test_cup_glow.py tests/test_tuck_lantern.py tests/test_smooth_drape.py tests/test_drape_loops.py
```
