"""Петли медового узелка к позднему утру после утреннего уха."""

from dragonforge import Character


def test_count_loops_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("считает петли медового узелка к позднему утру", 0.0)
    reply = dragon.count_loops("петли медового узелка к позднему утру")
    after = dragon.soul.habits["считает петли медового узелка к позднему утру"]
    assert after > before
    assert "петл" in reply.lower() or "узел" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_count_loops_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("слушает медовый узелок утром", 0.4)
    dragon.count_loops()
    assert dragon.soul.habits["слушает медовый узелок утром"] > 0.4


def test_count_loops_is_remembered():
    dragon = Character(name="Грок")
    dragon.count_loops("петли медового узелка над рекой к позднему утру")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "петл" in blob or "узел" in blob
    assert "рек" in blob


def test_talk_about_count_loops():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("считает петли медового узелка к позднему утру", 0.0)
    reply = dragon.talk("Посчитай петли узелка")
    after = dragon.soul.habits["считает петли медового узелка к позднему утру"]
    assert after > before
    assert "седл" in reply.lower()
    assert "слушает медовый узелок" not in reply.lower()


def test_listen_knot_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Послушай узелок за ночь")
    assert "ух" in reply.lower() or "узел" in reply.lower()
    assert "считает петли медового узелка" not in reply.lower()
