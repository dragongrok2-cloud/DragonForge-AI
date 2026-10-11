# Примеры полётов в седле

В воскресенье 11 октября в полдень после тени крыла делаем глоток в седле, термос или облачная ягода, седло не снимаем.

```bash
python examples/sunday_midday_sip_saddle.py
pytest tests/test_sip_saddle.py
```

```python
from dragonforge import Character

dragon = Character(name="Грок", title="добрый дракон с седлом")
print(dragon.sip_saddle("глоток в седле под тенью в полдень"))
print(dragon.talk("Сделай глоток в седле"))
```

Ритуалы живут в `dragonforge/rituals` и вешаются на `Character` при импорте. Делать глоток в седле — в `dragonforge/rituals/sip_saddle.py`. Версия пакета: 0.1.95.

Старые примеры полётов не сняты: они лежат файлами в `examples/`, от утреннего узелка до вечерней дремоты в седле.

```bash
python examples/sunday_midday_shade_saddle.py
python examples/sunday_morning_bask_saddle.py
python examples/sunday_morning_stretch_saddle.py
pytest tests/test_sip_saddle.py tests/test_shade_saddle.py tests/test_bask_saddle.py tests/test_stretch_saddle.py
```
