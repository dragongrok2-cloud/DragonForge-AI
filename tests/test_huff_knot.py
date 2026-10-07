"""Дыхание на медовый узелок к позднему дню после тихого узла."""

from dragonforge import Character


def test_huff_knot_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("согревает медовый узелок к позднему дню", 0.0)
    reply = dragon.huff_knot("дыхание на медовый узелок к позднему дню")
    after = dragon.soul.habits["согревает медовый узелок к позднему дню"]
    assert after > before
    assert "узел" in reply.lower() or "дых" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_huff_knot_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("завязывает узелок на медовом хвостике к позднему дню", 0.4)
    dragon.huff_knot()
    assert dragon.soul.habits["завязывает узелок на медовом хвостике к позднему дню"] > 0.4


def test_huff_knot_is_remembered():
    dragon = Character(name="Грок")
    dragon.huff_knot("дыхание на медовый узелок над рекой к позднему дню")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "узел" in blob or "дых" in blob
    assert "рек" in blob


def test_talk_about_huff_knot():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("согревает медовый узелок к позднему дню", 0.0)
    reply = dragon.talk("Подыши на узелок, чтобы не стыл")
    after = dragon.soul.habits["согревает медовый узелок к позднему дню"]
    assert after > before
    assert "седл" in reply.lower()
    assert "завязывает узелок" not in reply.lower()


def test_knot_thread_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Завяжи медовый узелок, подворот не трогай")
    assert "узел" in reply.lower() or "нит" in reply.lower()
    assert "согревает медовый узелок" not in reply.lower()
