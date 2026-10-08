"""Ухо к медовому узелку утром после ночи."""

from dragonforge import Character


def test_listen_knot_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("слушает медовый узелок утром", 0.0)
    reply = dragon.listen_knot("ухо к медовому узелку утром")
    after = dragon.soul.habits["слушает медовый узелок утром"]
    assert after > before
    assert "узел" in reply.lower() or "ух" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_listen_knot_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("постукивает по тёплому узелку к вечеру", 0.4)
    dragon.listen_knot()
    assert dragon.soul.habits["постукивает по тёплому узелку к вечеру"] > 0.4


def test_listen_knot_is_remembered():
    dragon = Character(name="Грок")
    dragon.listen_knot("ухо к медовому узелку над рекой утром")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "узел" in blob or "ух" in blob
    assert "рек" in blob


def test_talk_about_listen_knot():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("слушает медовый узелок утром", 0.0)
    reply = dragon.talk("Послушай узелок за ночь")
    after = dragon.soul.habits["слушает медовый узелок утром"]
    assert after > before
    assert "седл" in reply.lower()
    assert "постукивает по тёплому узелку" not in reply.lower()


def test_tap_knot_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Постучи по узелку, он на месте?")
    assert "ког" in reply.lower() or "узел" in reply.lower()
    assert "слушает медовый узелок" not in reply.lower()
