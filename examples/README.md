# Примеры полётов в седле

После полудня 9 октября крошка уже лежала на полоске солнца. Смахиваем пыльцу краем крыла, не вытаскивая фонарик и не снимая седла.

```bash
python examples/friday_afternoon_sweep_crumb.py
pytest tests/test_sweep_crumb.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.sweep_crumb("крошка с полоски солнца после полудня"))
print(dragon.talk("Смахни крошку после полудня"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Смахивание крошки — в `dragonforge/rituals/sweep_crumb.py`. Версия пакета: 0.1.76.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до яблочной крошки на полоске солнца.

```bash
python examples/friday_noon_share_crumb.py
python examples/friday_eleven_tilt_glass.py
python examples/friday_midmorning_blot_bead.py
python examples/friday_morning_cup_glow.py
pytest tests/test_sweep_crumb.py tests/test_share_crumb.py tests/test_tilt_glass.py tests/test_blot_bead.py
```
