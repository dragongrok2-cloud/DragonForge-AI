"""Стежки на тёплой складке утром после поглаживания."""

from dragonforge import Character


def test_count_stitch_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("считает стежки на тёплой складке утром", 0.0)
    reply = dragon.count_stitch("стежки на тёплой складке утром")
    after = dragon.soul.habits["считает стежки на тёплой складке утром"]
    assert after > before
    assert "стеж" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_count_stitch_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("поглаживает тёплую складку ремня утром", 0.4)
    dragon.count_stitch()
    assert dragon.soul.habits["поглаживает тёплую складку ремня утром"] > 0.4


def test_count_stitch_is_remembered():
    dragon = Character(name="Грок")
    dragon.count_stitch("стежки на тёплой складке над рекой утром")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "стеж" in blob
    assert "рек" in blob


def test_talk_about_count_stitch():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("считает стежки на тёплой складке утром", 0.0)
    reply = dragon.talk("Посчитай стежки на складке, подворот не трогай")
    after = dragon.soul.habits["считает стежки на тёплой складке утром"]
    assert after > before
    assert "стеж" in reply.lower()
    assert "седл" in reply.lower()


def test_pat_fold_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Погладь тёплую складку утром, подворот не трогай")
    assert "складк" in reply.lower()
    assert "считает стежки" not in reply.lower()
