"""Тесты ритуала circle_short."""

from dragonforge import Character


def test_circle_short_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("делает короткий круг после тёплого выдоха", 0.0)
    text = dragon.circle_short("короткий круг над лугом")
    after = dragon.soul.habits["делает короткий круг после тёплого выдоха"]
    assert after > before
    assert "короткий круг над лугом" in text
    assert "круг" in text.lower()


def test_circle_short_default_loop():
    dragon = Character(name="Грок")
    text = dragon.circle_short("  ")
    assert "короткий круг над лугом" in text


def test_circle_short_is_remembered():
    dragon = Character(name="Грок")
    dragon.circle_short("короткий круг над хребтом")
    recalled = dragon.memory.recall("круг", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "круг" in blob or "хреб" in blob


def test_talk_about_short_circle():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("делает короткий круг после тёплого выдоха", 0.0)
    reply = dragon.talk("Сделай короткий круг над гнездом")
    after = dragon.soul.habits["делает короткий круг после тёплого выдоха"]
    assert after > before
    assert "гнезд" in reply.lower()
    assert "круг" in reply.lower()
