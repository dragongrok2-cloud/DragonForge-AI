# Примеры полётов в седле

В воскресенье 11 октября утром мягко потягиваемся в седле под солнцем, крылья чуть шире раскрываем, седло не снимаем.

```bash
python examples/sunday_morning_stretch_saddle.py
pytest tests/test_stretch_saddle.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.stretch_saddle("седло под утренним солнцем"))
print(dragon.talk("Потянись в седле"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Потягивание в седле — в `dragonforge/rituals/stretch_saddle.py`. Версия пакета: 0.1.92.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до вечерней дремоты в седле.

```bash
python examples/saturday_evening_drowse_saddle.py
python examples/saturday_evening_nestle_saddle.py
pytest tests/test_stretch_saddle.py tests/test_drowse_saddle.py tests/test_nestle_saddle.py
```
