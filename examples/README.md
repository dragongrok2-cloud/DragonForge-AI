# Примеры полётов в седле

Короткие сцены, в которых привычка крепнет, а седло не снимают.

## 6 октября, утро

Ладонь уже поднята с чешуйки. Капля росы ещё на крае — её промокаем крылом, перчатка не липнет.

```bash
python examples/tuesday_blot_scale.py
pytest tests/test_blot_scale.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.blot_scale("роса с чешуйки после ладони"))
print(dragon.talk("Промокни чешуйку после ладони"))
```

Ритуал живёт в `dragonforge/rituals` и вешается на `Character` при импорте. Версия пакета: 0.1.47.
