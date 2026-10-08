"""Край попоны на согретые петли медового узелка к середине дня 8 октября."""

from dragonforge import Character


def test_drape_loops_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("накрывает согретые петли краем попоны к середине дня", 0.0)
    reply = dragon.drape_loops("край попоны на петлях медового узелка к середине дня")
    after = dragon.soul.habits["накрывает согретые петли краем попоны к середине дня"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_drape_loops_keeps_warm_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("согревает петли медового узелка дыханием к позднему дню", 0.4)
    dragon.drape_loops()
    assert dragon.soul.habits["согревает петли медового узелка дыханием к позднему дню"] > 0.4


def test_drape_loops_is_remembered():
    dragon = Character(name="Грок")
    dragon.drape_loops("край попоны на петлях медового узелка над рекой к середине дня")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "петл" in blob or "узел" in blob
    assert "рек" in blob


def test_talk_about_drape_loops():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("накрывает согретые петли краем попоны к середине дня", 0.0)
    reply = dragon.talk("Накрой петли узелка попоной")
    after = dragon.soul.habits["накрывает согретые петли краем попоны к середине дня"]
    assert after > before
    assert "седл" in reply.lower()
    assert "согревает петли медового узелка дыханием" not in reply.lower()


def test_warm_loops_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Согрей петли узелка")
    assert "петл" in reply.lower() or "узел" in reply.lower()
    assert "накрывает согретые петли" not in reply.lower()
