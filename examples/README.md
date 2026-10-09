# Примеры полётов в седле

После полудня 9 октября полоска уже лежит на костяшках. Сгибаем пальцы один раз, чтобы свет лёг в сгиб, не вытаскивая фонарик и не снимая седла.

```bash
python examples/friday_afternoon_curl_fingers.py
pytest tests/test_curl_fingers.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.curl_fingers("пальцы в полоске солнца после полудня"))
print(dragon.talk("Согни пальцы в полоске"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Сгиб пальцев — в `dragonforge/rituals/curl_fingers.py`. Версия пакета: 0.1.79.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до полоски на костяшках.

```bash
python examples/friday_afternoon_shift_stripe.py
python examples/friday_afternoon_rest_stripe.py
python examples/friday_afternoon_sweep_crumb.py
pytest tests/test_curl_fingers.py tests/test_shift_stripe.py tests/test_rest_stripe.py
```
