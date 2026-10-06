# Примеры полётов в седле

Короткие сцены, в которых привычка крепнет, а седло не снимают.

## 6 октября, к полудню

Роса с чешуйки уже промокнута. Край попоны складываем под луку, чтобы ветер его не поднимал.

```bash
python examples/tuesday_fold_cloth.py
pytest tests/test_fold_cloth.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.fold_cloth("край попоны под лукой после росы"))
print(dragon.talk("Сложи край попоны после росы"))
```

## 6 октября, утро

Ладонь уже поднята с чешуйки. Капля росы ещё на крае — её промокаем крылом, перчатка не липнет.

```bash
python examples/tuesday_blot_scale.py
pytest tests/test_blot_scale.py
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Версия пакета: 0.1.48.
