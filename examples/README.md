# Примеры полётов в седле

К полудню 9 октября полоска солнца уже легла на сухое стекло. Кладём на неё тёплую яблочную крошку, не вытаскивая фонарик и не снимая седла.

```bash
python examples/friday_noon_share_crumb.py
pytest tests/test_share_crumb.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.share_crumb("яблочная крошка на полоске солнца в полдень"))
print(dragon.talk("Поделись крошкой в полдень"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Крошка на полоске — в `dragonforge/rituals/share_crumb.py`. Версия пакета: 0.1.75.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до полоски солнца на сухом стекле.

```bash
python examples/friday_eleven_tilt_glass.py
python examples/friday_midmorning_blot_bead.py
python examples/friday_morning_cup_glow.py
python examples/thursday_evening_tuck_lantern.py
pytest tests/test_share_crumb.py tests/test_tilt_glass.py tests/test_blot_bead.py tests/test_cup_glow.py
```
