# Примеры полётов в седле

К вечеру 10 октября после опоры на луку уютно устраиваемся в седле, крылья чуть складываем, седло не снимаем, слушаем закат.

```bash
python examples/saturday_evening_nestle_saddle.py
pytest tests/test_nestle_saddle.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.nestle_saddle("седло к вечеру после луки"))
print(dragon.talk("Устройся в седле"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Уют в седле — в `dragonforge/rituals/nestle_saddle.py`. Версия пакета: 0.1.90.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до вечернего уюта в седле.

```bash
python examples/saturday_afternoon_settle_pommel.py
python examples/saturday_afternoon_stroke_pommel.py
pytest tests/test_nestle_saddle.py tests/test_settle_pommel.py tests/test_stroke_pommel.py
```
