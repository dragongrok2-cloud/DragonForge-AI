# Примеры полётов в седле

В воскресенье 11 октября утром после потягивания посидим и погреемся в седле под солнцем, крылья чуть раскрыты, седло не снимаем.

```bash
python examples/sunday_morning_bask_saddle.py
pytest tests/test_bask_saddle.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.bask_saddle("седло под утренним солнцем"))
print(dragon.talk("Погрейся в седле"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Греться в седле — в `dragonforge/rituals/bask_saddle.py`. Версия пакета: 0.1.93.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до вечерней дремоты в седле.

```bash
python examples/sunday_morning_stretch_saddle.py
python examples/saturday_evening_drowse_saddle.py
pytest tests/test_bask_saddle.py tests/test_stretch_saddle.py tests/test_drowse_saddle.py
```
