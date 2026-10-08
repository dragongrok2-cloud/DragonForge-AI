"""Дыхание на затенённые петли медового узелка к позднему дню 8 октября."""

from dragonforge import Character


def test_warm_loops_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("согревает петли медового узелка дыханием к позднему дню", 0.0)
    reply = dragon.warm_loops("дыхание на петлях медового узелка к позднему дню")
    after = dragon.soul.habits["согревает петли медового узелка дыханием к позднему дню"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_warm_loops_keeps_shade_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("накрывает петли медового узелка тенью после полудня", 0.4)
    dragon.warm_loops()
    assert dragon.soul.habits["накрывает петли медового узелка тенью после полудня"] > 0.4


def test_warm_loops_is_remembered():
    dragon = Character(name="Грок")
    dragon.warm_loops("дыхание на петлях медового узелка над рекой к позднему дню")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "петл" in blob or "узел" in blob
    assert "рек" in blob


def test_talk_about_warm_loops():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("согревает петли медового узелка дыханием к позднему дню", 0.0)
    reply = dragon.talk("Согрей петли узелка")
    after = dragon.soul.habits["согревает петли медового узелка дыханием к позднему дню"]
    assert after > before
    assert "седл" in reply.lower()
    assert "накрывает петли медового узелка" not in reply.lower()


def test_shade_loops_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Затени петли узелка")
    assert "петл" in reply.lower() or "узел" in reply.lower()
    assert "согревает петли медового узелка" not in reply.lower()
