# Примеры полётов в седле

К вечеру 9 октября сгиб уже разжат на Мёде, Шве и Седле. Только кладём тёплую ладонь на луку один раз, чтобы тепло сгиба осталось на коже, не вытаскивая фонарик и не снимая седла.

```bash
python examples/friday_evening_lay_warmth.py
pytest tests/test_lay_warmth.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.lay_warmth("тепло сгиба на луке к вечеру"))
print(dragon.talk("Положи тепло на луку к вечеру"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Тепло на луке — в `dragonforge/rituals/lay_warmth.py`. Версия пакета: 0.1.81.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до разжатого сгиба.

```bash
python examples/friday_evening_ease_fold.py
python examples/friday_afternoon_curl_fingers.py
pytest tests/test_lay_warmth.py tests/test_ease_fold.py tests/test_curl_fingers.py
```
