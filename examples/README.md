# Примеры полётов в седле

В воскресенье 11 октября в полдень после утреннего баска даём тень крылом в седле, крылья чуть сложены для прохлады, седло не снимаем.

```bash
python examples/sunday_midday_shade_saddle.py
pytest tests/test_shade_saddle.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.shade_saddle("седло под крылом в полдень"))
print(dragon.talk("Дай тень в седле"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Давать тень в седле — в `dragonforge/rituals/shade_saddle.py`. Версия пакета: 0.1.94.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до вечерней дремоты в седле.

```bash
python examples/sunday_morning_bask_saddle.py
python examples/sunday_morning_stretch_saddle.py
pytest tests/test_shade_saddle.py tests/test_bask_saddle.py tests/test_stretch_saddle.py
```
