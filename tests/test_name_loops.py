"""Имена петель медового узелка к раннему дню после обвода."""

from dragonforge import Character


def test_name_loops_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("называет петли медового узелка к раннему дню", 0.0)
    reply = dragon.name_loops("имена петель медового узелка к раннему дню")
    after = dragon.soul.habits["называет петли медового узелка к раннему дню"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_name_loops_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("обводит петли медового узелка к полудню", 0.4)
    dragon.name_loops()
    assert dragon.soul.habits["обводит петли медового узелка к полудню"] > 0.4


def test_name_loops_is_remembered():
    dragon = Character(name="Грок")
    dragon.name_loops("имена петель медового узелка над рекой к раннему дню")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "петл" in blob or "узел" in blob
    assert "рек" in blob


def test_talk_about_name_loops():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("называет петли медового узелка к раннему дню", 0.0)
    reply = dragon.talk("Назови петли узелка")
    after = dragon.soul.habits["называет петли медового узелка к раннему дню"]
    assert after > before
    assert "седл" in reply.lower()
    assert "обводит петли медового узелка" not in reply.lower()


def test_trace_loops_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Обведи петли узелка")
    assert "петл" in reply.lower() or "узел" in reply.lower()
    assert "называет петли медового узелка" not in reply.lower()
