# Примеры полётов в седле

В воскресенье 11 октября после полудня опираемся спиной на луку в седле под тенью крыла, седло не снимаем.

```bash
python examples/sunday_afternoon_lean_saddle.py
pytest tests/test_lean_saddle.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.lean_saddle("опирание спиной на луку в седле под тенью после полудня"))
print(dragon.talk("Опрись в седле"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Опираться спиной на луку в седле — в `dragonforge/rituals/lean_saddle.py`. Версия пакета: 0.1.98.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до вечерней дремоты в седле.

```bash
python examples/sunday_afternoon_hum_saddle.py
python examples/sunday_afternoon_gaze_saddle.py
python examples/sunday_midday_sip_saddle.py
python examples/sunday_midday_shade_saddle.py
python examples/sunday_morning_bask_saddle.py
python examples/sunday_morning_stretch_saddle.py
pytest tests/test_lean_saddle.py tests/test_hum_saddle.py tests/test_gaze_saddle.py tests/test_sip_saddle.py tests/test_shade_saddle.py tests/test_bask_saddle.py tests/test_stretch_saddle.py
```
