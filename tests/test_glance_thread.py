"""Медовый хвостик в послеполуденном свете после прижатого конца."""

from dragonforge import Character


def test_glance_thread_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("глядит медовый хвостик в послеполуденном свете", 0.0)
    reply = dragon.glance_thread("медовый хвостик в послеполуденном свете")
    after = dragon.soul.habits["глядит медовый хвостик в послеполуденном свете"]
    assert after > before
    assert "нит" in reply.lower() or "хвостик" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_glance_thread_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("прижимает конец нитки к полудню", 0.4)
    dragon.glance_thread()
    assert dragon.soul.habits["прижимает конец нитки к полудню"] > 0.4


def test_glance_thread_is_remembered():
    dragon = Character(name="Грок")
    dragon.glance_thread("медовый хвостик над рекой в послеполуденном свете")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "хвостик" in blob or "нит" in blob
    assert "рек" in blob


def test_talk_about_glance_thread():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("глядит медовый хвостик в послеполуденном свете", 0.0)
    reply = dragon.talk("Глянь шов в послеполуденном свете, подворот не трогай")
    after = dragon.soul.habits["глядит медовый хвостик в послеполуденном свете"]
    assert after > before
    assert "седл" in reply.lower()
    assert "прижимает конец нитки" not in reply.lower()


def test_tuck_thread_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Прижми конец нитки под стежки, подворот не трогай")
    assert "нит" in reply.lower()
    assert "глядит медовый хвостик" not in reply.lower()
