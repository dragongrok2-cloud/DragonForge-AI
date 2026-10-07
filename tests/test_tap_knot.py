"""Коготь по тёплому узелку к вечеру после дыхания."""

from dragonforge import Character


def test_tap_knot_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("постукивает по тёплому узелку к вечеру", 0.0)
    reply = dragon.tap_knot("коготь по тёплому узелку к вечеру")
    after = dragon.soul.habits["постукивает по тёплому узелку к вечеру"]
    assert after > before
    assert "узел" in reply.lower() or "ког" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_tap_knot_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("согревает медовый узелок к позднему дню", 0.4)
    dragon.tap_knot()
    assert dragon.soul.habits["согревает медовый узелок к позднему дню"] > 0.4


def test_tap_knot_is_remembered():
    dragon = Character(name="Грок")
    dragon.tap_knot("коготь по тёплому узелку над рекой к вечеру")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "узел" in blob or "ког" in blob
    assert "рек" in blob


def test_talk_about_tap_knot():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("постукивает по тёплому узелку к вечеру", 0.0)
    reply = dragon.talk("Постучи по узелку, он на месте?")
    after = dragon.soul.habits["постукивает по тёплому узелку к вечеру"]
    assert after > before
    assert "седл" in reply.lower()
    assert "согревает медовый узелок" not in reply.lower()


def test_huff_knot_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Подыши на узелок, чтобы не стыл")
    assert "дых" in reply.lower() or "узел" in reply.lower()
    assert "постукивает по тёплому узелку" not in reply.lower()
