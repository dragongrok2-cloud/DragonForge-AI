"""Тёплый ремень после подвёрнутого конца."""

from dragonforge import Character


def test_warm_strap_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("согревает подвёрнутый ремень к вечеру", 0.0)
    reply = dragon.warm_strap("подвёрнутый ремень к вечеру")
    after = dragon.soul.habits["согревает подвёрнутый ремень к вечеру"]
    assert after > before
    assert "ремень" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_warm_strap_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("подворачивает конец ремня после тихой пряжки", 0.4)
    dragon.warm_strap()
    assert dragon.soul.habits["подворачивает конец ремня после тихой пряжки"] > 0.4


def test_warm_strap_is_remembered():
    dragon = Character(name="Грок")
    dragon.warm_strap("подвёрнутый ремень над рекой к вечеру")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "ремень" in blob
    assert "рек" in blob


def test_talk_about_warm_strap():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("согревает подвёрнутый ремень к вечеру", 0.0)
    reply = dragon.talk("Согрей подвёрнутый ремень, чтобы не стыл")
    after = dragon.soul.habits["согревает подвёрнутый ремень к вечеру"]
    assert after > before
    assert "ремень" in reply.lower()
    assert "седл" in reply.lower()


def test_tuck_strap_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Подогни конец ремня, чтобы не хлопал")
    assert "ремн" in reply.lower()
    assert "согревает подвёрнутый ремень" not in reply.lower()
