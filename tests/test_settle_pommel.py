"""Опереться ладонью на луку в субботу 10 октября после полудня."""

from dragonforge import Character


def test_settle_pommel_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("опирается ладонью на луку после полудня", 0.0)
    reply = dragon.settle_pommel("луку после поглаживания")
    after = dragon.soul.habits["опирается ладонью на луку после полудня"]
    assert after > before
    assert "лук" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "ладон" in reply.lower() or "опир" in reply.lower()


def test_settle_pommel_keeps_stroke_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("гладит луку ладонью после полудня", 0.4)
    dragon.settle_pommel()
    assert dragon.soul.habits.get("гладит луку ладонью после полудня", 0.0) >= 0.4


def test_settle_pommel_is_remembered():
    dragon = Character(name="Грок")
    dragon.settle_pommel("луку над рекой после поглаживания")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "лук" in blob or "ладон" in blob
    assert "рек" in blob


def test_talk_about_settle_pommel():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("опирается ладонью на луку после полудня", 0.0)
    reply = dragon.talk("Опрись на луку")
    after = dragon.soul.habits["опирается ладонью на луку после полудня"]
    assert after > before
    assert "седл" in reply.lower()
