# Примеры полётов в седле

К одиннадцати 9 октября бусинка росы уже ушла со стекла. Только наклоняем сухое стекло под краем, чтобы полоска солнца легла на седло, не вытаскивая фонарик и не снимая седла.

```bash
python examples/friday_eleven_tilt_glass.py
pytest tests/test_tilt_glass.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.tilt_glass("полоска солнца на сухом стекле к одиннадцати"))
print(dragon.talk("Наклони стекло к одиннадцати"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Полоска солнца на сухом стекле — в `dragonforge/rituals/tilt_glass.py`. Версия пакета: 0.1.74.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до бусинки росы.

```bash
python examples/friday_midmorning_blot_bead.py
python examples/friday_morning_cup_glow.py
python examples/thursday_evening_tuck_lantern.py
python examples/thursday_evening_smooth_drape.py
python examples/thursday_drape_loops.py
python examples/thursday_warm_loops.py
pytest tests/test_tilt_glass.py tests/test_blot_bead.py tests/test_cup_glow.py tests/test_tuck_lantern.py
```
