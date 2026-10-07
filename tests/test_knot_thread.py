"""Узелок на медовом хвостике к позднему дню после взгляда в свет."""

from dragonforge import Character


def test_knot_thread_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("завязывает узелок на медовом хвостике к позднему дню", 0.0)
    reply = dragon.knot_thread("узелок на медовом хвостике к позднему дню")
    after = dragon.soul.habits["завязывает узелок на медовом хвостике к позднему дню"]
    assert after > before
    assert "узел" in reply.lower() or "нит" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_knot_thread_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("глядит медовый хвостик в послеполуденном свете", 0.4)
    dragon.knot_thread()
    assert dragon.soul.habits["глядит медовый хвостик в послеполуденном свете"] > 0.4


def test_knot_thread_is_remembered():
    dragon = Character(name="Грок")
    dragon.knot_thread("узелок на медовом хвостике над рекой к позднему дню")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "узел" in blob or "нит" in blob
    assert "рек" in blob


def test_talk_about_knot_thread():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("завязывает узелок на медовом хвостике к позднему дню", 0.0)
    reply = dragon.talk("Завяжи медовый узелок, подворот не трогай")
    after = dragon.soul.habits["завязывает узелок на медовом хвостике к позднему дню"]
    assert after > before
    assert "седл" in reply.lower()
    assert "глядит медовый хвостик" not in reply.lower()


def test_glance_thread_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Глянь шов в послеполуденном свете, подворот не трогай")
    assert "нит" in reply.lower() or "хвостик" in reply.lower()
    assert "завязывает узелок" not in reply.lower()
