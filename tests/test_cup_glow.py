"""Ладони о стекло фонарика под краем попоны утром 9 октября."""

from dragonforge import Character


def test_cup_glow_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("согревает ладони о стекло фонарика под краем утром", 0.0)
    reply = dragon.cup_glow("ладони о стекло фонарика под краем попоны утром")
    after = dragon.soul.habits["согревает ладони о стекло фонарика под краем утром"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_cup_glow_keeps_lantern_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("подтыкает фонарик под разглаженный край попоны к вечеру", 0.4)
    dragon.cup_glow()
    assert dragon.soul.habits["подтыкает фонарик под разглаженный край попоны к вечеру"] > 0.4


def test_cup_glow_is_remembered():
    dragon = Character(name="Грок")
    dragon.cup_glow("ладони о стекло фонарика над рекой утром")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "стекл" in blob or "ладон" in blob
    assert "рек" in blob


def test_talk_about_cup_glow():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("согревает ладони о стекло фонарика под краем утром", 0.0)
    reply = dragon.talk("Согрей ладони о стекло фонарика")
    after = dragon.soul.habits["согревает ладони о стекло фонарика под краем утром"]
    assert after > before
    assert "седл" in reply.lower()
    assert "подтыкает фонарик" not in reply.lower()


def test_tuck_lantern_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Подсунь фонарик под край попоны")
    assert "фонар" in reply.lower() or "край" in reply.lower()
    assert "согревает ладони" not in reply.lower()


def test_light_lantern_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Зажги фонарик на седле")
    assert "фонар" in reply.lower() or "седл" in reply.lower()
    assert "согревает ладони о стекло" not in reply.lower()
