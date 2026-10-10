"""Обвести луку утром 10 октября после глажки."""

from dragonforge import Character


def test_trace_pommel_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("обводит луку утром после глажки", 0.0)
    reply = dragon.trace_pommel("луку утром после глажки")
    after = dragon.soul.habits["обводит луку утром после глажки"]
    assert after > before
    assert "лук" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "когт" in reply.lower() or "обвод" in reply.lower()


def test_trace_pommel_keeps_pat_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("гладит луку утром после тепла", 0.4)
    dragon.trace_pommel()
    assert dragon.soul.habits["гладит луку утром после тепла"] > 0.4


def test_trace_pommel_is_remembered():
    dragon = Character(name="Грок")
    dragon.trace_pommel("луку над рекой утром после глажки")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "лук" in blob or "обвод" in blob
    assert "рек" in blob


def test_talk_about_trace_pommel():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("обводит луку утром после глажки", 0.0)
    reply = dragon.talk("Обведи луку утром")
    after = dragon.soul.habits["обводит луку утром после глажки"]
    assert after > before
    assert "седл" in reply.lower()
    assert "гладит луку" not in reply.lower()


def test_pat_pommel_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Погладь луку утром")
    assert "лук" in reply.lower()
    assert "обводит луку" not in reply.lower()
