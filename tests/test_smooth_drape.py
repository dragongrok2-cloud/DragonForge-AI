"""Ладонь по краю попоны на согретых петлях к вечеру 8 октября."""

from dragonforge import Character


def test_smooth_drape_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("гладит край попоны на согретых петлях к вечеру", 0.0)
    reply = dragon.smooth_drape("край попоны на петлях медового узелка к вечеру")
    after = dragon.soul.habits["гладит край попоны на согретых петлях к вечеру"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_smooth_drape_keeps_drape_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("накрывает согретые петли краем попоны к середине дня", 0.4)
    dragon.smooth_drape()
    assert dragon.soul.habits["накрывает согретые петли краем попоны к середине дня"] > 0.4


def test_smooth_drape_is_remembered():
    dragon = Character(name="Грок")
    dragon.smooth_drape("край попоны на петлях медового узелка над рекой к вечеру")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "петл" in blob or "узел" in blob
    assert "рек" in blob


def test_talk_about_smooth_drape():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("гладит край попоны на согретых петлях к вечеру", 0.0)
    reply = dragon.talk("Погладь край попоны на петлях")
    after = dragon.soul.habits["гладит край попоны на согретых петлях к вечеру"]
    assert after > before
    assert "седл" in reply.lower()
    assert "накрывает согретые петли" not in reply.lower()


def test_drape_loops_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Накрой петли узелка попоной")
    assert "петл" in reply.lower() or "узел" in reply.lower()
    assert "гладит край попоны" not in reply.lower()


def test_pat_fold_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Погладь складку ремня")
    assert "складк" in reply.lower() or "ремн" in reply.lower()
    assert "гладит край попоны" not in reply.lower()
