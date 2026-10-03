"""Тесты ритуала catch_thermal."""

from dragonforge import Character


def test_catch_thermal_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("ловит термик после горизонта", 0.0)
    text = dragon.catch_thermal("тёплый столб над лугом")
    after = dragon.soul.habits["ловит термик после горизонта"]
    assert after > before
    assert "тёплый столб над лугом" in text
    assert "термик" in text.lower()


def test_catch_thermal_default_lift():
    dragon = Character(name="Грок")
    text = dragon.catch_thermal("  ")
    assert "тёплый столб над лугом" in text


def test_catch_thermal_is_remembered():
    dragon = Character(name="Грок")
    dragon.catch_thermal("термик над речной излучиной")
    recalled = dragon.memory.recall("термик", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "термик" in blob or "излучин" in blob


def test_talk_about_thermal_catches():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("ловит термик после горизонта", 0.0)
    reply = dragon.talk("Поймай термик у скалы")
    after = dragon.soul.habits["ловит термик после горизонта"]
    assert after > before
    assert "термик" in reply.lower() or "столб" in reply.lower()
    assert "скал" in reply.lower()
