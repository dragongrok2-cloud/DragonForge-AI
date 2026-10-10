"""Дремать в седле в субботу 10 октября к ночи."""

from dragonforge import Character


def test_drowse_saddle_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("дремлет в седле к ночи", 0.0)
    reply = dragon.drowse_saddle("седло к ночи после уюта")
    after = dragon.soul.habits["дремлет в седле к ночи"]
    assert after > before
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "дрем" in reply.lower() or "ноч" in reply.lower()


def test_drowse_saddle_keeps_nestle_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("уютно устраивается в седле к вечеру", 0.4)
    dragon.drowse_saddle()
    assert dragon.soul.habits.get("уютно устраивается в седле к вечеру", 0.0) >= 0.4


def test_drowse_saddle_is_remembered():
    dragon = Character(name="Грок")
    dragon.drowse_saddle("седло под звёздами к ночи")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "седл" in blob or "дрем" in blob
    assert "звезд" in blob or "звёзд" in blob


def test_talk_about_drowse_saddle():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("дремлет в седле к ночи", 0.0)
    reply = dragon.talk("Дремли в седле")
    after = dragon.soul.habits["дремлет в седле к ночи"]
    assert after > before
    assert "седл" in reply.lower()
