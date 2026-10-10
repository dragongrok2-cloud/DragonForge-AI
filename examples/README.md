# Примеры полётов в седле

К послеполудню 10 октября лука уже поглажена ладонью. Тихо опираемся ладонью на тёплую луку, седло не снимаем, дышим вместе.

```bash
python examples/saturday_afternoon_settle_pommel.py
pytest tests/test_settle_pommel.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.settle_pommel("луку после поглаживания"))
print(dragon.talk("Опрись на луку"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Опора на луке — в `dragonforge/rituals/settle_pommel.py`. Версия пакета: 0.1.89.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до поглаженной луки.

```bash
python examples/saturday_afternoon_stroke_pommel.py
python examples/saturday_october_10_nuzzle_pommel.py
pytest tests/test_settle_pommel.py tests/test_stroke_pommel.py tests/test_nuzzle_pommel.py
```
