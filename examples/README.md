# Примеры полётов в седле

В воскресенье 11 октября в полдень после глотка в седле смотрим на горизонт из седла под тенью крыла, седло не снимаем.

```bash
python examples/sunday_afternoon_gaze_saddle.py
pytest tests/test_gaze_saddle.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.gaze_saddle("взгляд на горизонт из седла под тенью в полдень"))
print(dragon.talk("Посмотри на горизонт"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Смотреть на горизонт из седла — в `dragonforge/rituals/gaze_saddle.py`. Версия пакета: 0.1.96.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до вечерней дремоты в седле.

```bash
python examples/sunday_midday_sip_saddle.py
python examples/sunday_midday_shade_saddle.py
python examples/sunday_morning_bask_saddle.py
python examples/sunday_morning_stretch_saddle.py
pytest tests/test_gaze_saddle.py tests/test_sip_saddle.py tests/test_shade_saddle.py tests/test_bask_saddle.py tests/test_stretch_saddle.py
```
