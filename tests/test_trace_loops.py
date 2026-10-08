"""Обвод петель медового узелка к полудню после счёта."""

from dragonforge import Character


def test_trace_loops_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("обводит петли медового узелка к полудню", 0.0)
    reply = dragon.trace_loops("коготь по петлям медового узелка к полудню")
    after = dragon.soul.habits["обводит петли медового узелка к полудню"]
    assert after > before
    assert "петл" in reply.lower() or "узел" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_trace_loops_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("считает петли медового узелка к позднему утру", 0.4)
    dragon.trace_loops()
    assert dragon.soul.habits["считает петли медового узелка к позднему утру"] > 0.4


def test_trace_loops_is_remembered():
    dragon = Character(name="Грок")
    dragon.trace_loops("коготь по петлям медового узелка над рекой к полудню")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "петл" in blob or "узел" in blob
    assert "рек" in blob


def test_talk_about_trace_loops():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("обводит петли медового узелка к полудню", 0.0)
    reply = dragon.talk("Обведи петли узелка")
    after = dragon.soul.habits["обводит петли медового узелка к полудню"]
    assert after > before
    assert "седл" in reply.lower()
    assert "считает петли медового узелка" not in reply.lower()


def test_count_loops_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Посчитай петли узелка")
    assert "петл" in reply.lower() or "узел" in reply.lower()
    assert "обводит петли медового узелка" not in reply.lower()
