# Примеры полётов в седле

После полудня 9 октября ладонь уже лежит на светлой полоске. Сдвигаем её на одну чешуйку, чтобы солнце согрело костяшки, не вытаскивая фонарик и не снимая седла.

```bash
python examples/friday_afternoon_shift_stripe.py
pytest tests/test_shift_stripe.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.shift_stripe("полоска солнца на костяшках после полудня"))
print(dragon.talk("Сдвинь полоску на костяшки"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Сдвиг полоски — в `dragonforge/rituals/shift_stripe.py`. Версия пакета: 0.1.78.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до ладони на светлой полоске.

```bash
python examples/friday_afternoon_rest_stripe.py
python examples/friday_afternoon_sweep_crumb.py
python examples/friday_noon_share_crumb.py
pytest tests/test_shift_stripe.py tests/test_rest_stripe.py tests/test_sweep_crumb.py
```
