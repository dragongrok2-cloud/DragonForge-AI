"""Потягиваться в седле в воскресенье 11 октября утром."""

from dragonforge import Character


def test_stretch_saddle_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("потягивается в седле по утрам", 0.0)
    reply = dragon.stretch_saddle("седло под утренним солнцем")
    after = dragon.soul.habits["потягивается в седле по утрам"]
    assert after > before
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "потяг" in reply.lower() or "солнц" in reply.lower()


def test_stretch_saddle_keeps_drowse_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("дремлет в седле к ночи", 0.4)
    dragon.stretch_saddle()
    assert dragon.soul.habits.get("дремлет в седле к ночи", 0.0) >= 0.4


def test_stretch_saddle_is_remembered():
    dragon = Character(name="Грок")
    dragon.stretch_saddle("седло под утренним солнцем")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "седл" in blob or "потяг" in blob
    assert "солнц" in blob


def test_talk_about_stretch_saddle():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("потягивается в седле по утрам", 0.0)
    reply = dragon.talk("Потянись в седле")
    after = dragon.soul.habits["потягивается в седле по утрам"]
    assert after > before
    assert "седл" in reply.lower()
