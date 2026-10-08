"""Фонарик под разглаженный край попоны к вечеру 8 октября."""

from dragonforge import Character


def test_tuck_lantern_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("подтыкает фонарик под разглаженный край попоны к вечеру", 0.0)
    reply = dragon.tuck_lantern("фонарик под разглаженный край попоны к вечеру")
    after = dragon.soul.habits["подтыкает фонарик под разглаженный край попоны к вечеру"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_tuck_lantern_keeps_smooth_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("гладит край попоны на согретых петлях к вечеру", 0.4)
    dragon.tuck_lantern()
    assert dragon.soul.habits["гладит край попоны на согретых петлях к вечеру"] > 0.4


def test_tuck_lantern_is_remembered():
    dragon = Character(name="Грок")
    dragon.tuck_lantern("фонарик под край попоны над рекой к вечеру")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "фонар" in blob or "край" in blob
    assert "рек" in blob


def test_talk_about_tuck_lantern():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("подтыкает фонарик под разглаженный край попоны к вечеру", 0.0)
    reply = dragon.talk("Подсунь фонарик под край попоны")
    after = dragon.soul.habits["подтыкает фонарик под разглаженный край попоны к вечеру"]
    assert after > before
    assert "седл" in reply.lower()
    assert "гладит край попоны" not in reply.lower()


def test_smooth_drape_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Погладь край попоны на петлях")
    assert "край" in reply.lower() or "попон" in reply.lower()
    assert "подтыкает фонарик" not in reply.lower()


def test_light_lantern_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Зажги фонарик на седле")
    assert "фонар" in reply.lower() or "седл" in reply.lower()
    assert "подтыкает фонарик под разглаженный" not in reply.lower()
