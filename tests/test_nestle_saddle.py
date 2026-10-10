"""Уютно устроиться в седле в субботу 10 октября к вечеру."""

from dragonforge import Character


def test_nestle_saddle_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("уютно устраивается в седле к вечеру", 0.0)
    reply = dragon.nestle_saddle("седло к вечеру после луки")
    after = dragon.soul.habits["уютно устраивается в седле к вечеру"]
    assert after > before
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "уют" in reply.lower() or "устраив" in reply.lower()


def test_nestle_saddle_keeps_settle_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("опирается ладонью на луку после полудня", 0.4)
    dragon.nestle_saddle()
    assert dragon.soul.habits.get("опирается ладонью на луку после полудня", 0.0) >= 0.4


def test_nestle_saddle_is_remembered():
    dragon = Character(name="Грок")
    dragon.nestle_saddle("седло над рекой к вечеру")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "седл" in blob or "уют" in blob
    assert "рек" in blob


def test_talk_about_nestle_saddle():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("уютно устраивается в седле к вечеру", 0.0)
    reply = dragon.talk("Устройся в седле")
    after = dragon.soul.habits["уютно устраивается в седле к вечеру"]
    assert after > before
    assert "седл" in reply.lower()
