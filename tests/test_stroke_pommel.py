"""Погладить луку ладонью в субботу 10 октября после полудня."""

from dragonforge import Character


def test_stroke_pommel_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("гладит луку ладонью после полудня", 0.0)
    reply = dragon.stroke_pommel("луку после полудня")
    after = dragon.soul.habits["гладит луку ладонью после полудня"]
    assert after > before
    assert "лук" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "ладон" in reply.lower() or "глад" in reply.lower()


def test_stroke_pommel_keeps_nuzzle_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("прижимает морду к луке после тёплого выдоха", 0.4)
    dragon.stroke_pommel()
    assert dragon.soul.habits.get("прижимает морду к луке после тёплого выдоха", 0.0) >= 0.4


def test_stroke_pommel_is_remembered():
    dragon = Character(name="Грок")
    dragon.stroke_pommel("луку над рекой после полудня")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "лук" in blob or "ладон" in blob
    assert "рек" in blob


def test_talk_about_stroke_pommel():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("гладит луку ладонью после полудня", 0.0)
    reply = dragon.talk("Погладь луку")
    after = dragon.soul.habits["гладит луку ладонью после полудня"]
    assert after > before
    assert "седл" in reply.lower()
