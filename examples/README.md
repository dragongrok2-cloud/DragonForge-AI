# Примеры полётов в седле

После полудня 9 октября крошка уже сметена с полоски солнца. Придерживаем ладонь на светлой полоске, не вытаскивая фонарик и не снимая седла.

```bash
python examples/friday_afternoon_rest_stripe.py
pytest tests/test_rest_stripe.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.rest_stripe("ладонь на светлой полоске после полудня"))
print(dragon.talk("Придержи ладонь на полоске"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Ладонь на полоске — в `dragonforge/rituals/rest_stripe.py`. Версия пакета: 0.1.77.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до смахивания крошки с полоски солнца.

```bash
python examples/friday_afternoon_sweep_crumb.py
python examples/friday_noon_share_crumb.py
python examples/friday_eleven_tilt_glass.py
pytest tests/test_rest_stripe.py tests/test_sweep_crumb.py tests/test_share_crumb.py
```
