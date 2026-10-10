# Примеры полётов в седле

К ночи 10 октября после уюта в седле мягко дремлем, крылья чуть сильнее складываем, седло не снимаем, слушаем звёзды.

```bash
python examples/saturday_evening_drowse_saddle.py
pytest tests/test_drowse_saddle.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.drowse_saddle("седло к ночи после уюта"))
print(dragon.talk("Дремли в седле"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Дремота в седле — в `dragonforge/rituals/drowse_saddle.py`. Версия пакета: 0.1.91.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до вечерней дремоты в седле.

```bash
python examples/saturday_evening_nestle_saddle.py
python examples/saturday_afternoon_settle_pommel.py
pytest tests/test_drowse_saddle.py tests/test_nestle_saddle.py tests/test_settle_pommel.py
```
