# Примеры полётов в седле

К вечеру 9 октября пальцы уже согнуты в полоске. Разжимаем сгиб один раз, чтобы тепло осталось на костяшках, не вытаскивая фонарик и не снимая седла.

```bash
python examples/friday_evening_ease_fold.py
pytest tests/test_ease_fold.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.ease_fold("сгиб полоски солнца к вечеру"))
print(dragon.talk("Разжми сгиб к вечеру"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Разжатый сгиб — в `dragonforge/rituals/ease_fold.py`. Версия пакета: 0.1.80.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до пальцев в полоске.

```bash
python examples/friday_afternoon_curl_fingers.py
python examples/friday_afternoon_shift_stripe.py
python examples/friday_afternoon_rest_stripe.py
pytest tests/test_ease_fold.py tests/test_curl_fingers.py tests/test_shift_stripe.py
```
