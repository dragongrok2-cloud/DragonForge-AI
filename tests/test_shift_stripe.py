"""Полоска солнца на костяшках после полудня 9 октября."""

from dragonforge import Character


def test_shift_stripe_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("сдвигает полоску солнца на костяшки после полудня", 0.0)
    reply = dragon.shift_stripe("полоска солнца на костяшках после полудня")
    after = dragon.soul.habits["сдвигает полоску солнца на костяшки после полудня"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "костяш" in reply.lower()


def test_shift_stripe_keeps_rest_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("держит ладонь на светлой полоске после полудня", 0.4)
    dragon.shift_stripe()
    assert dragon.soul.habits["держит ладонь на светлой полоске после полудня"] > 0.4


def test_shift_stripe_is_remembered():
    dragon = Character(name="Грок")
    dragon.shift_stripe("полоска солнца на костяшках над рекой после полудня")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "костяш" in blob
    assert "рек" in blob


def test_talk_about_shift_stripe():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("сдвигает полоску солнца на костяшки после полудня", 0.0)
    reply = dragon.talk("Сдвинь полоску на костяшки после полудня")
    after = dragon.soul.habits["сдвигает полоску солнца на костяшки после полудня"]
    assert after > before
    assert "седл" in reply.lower()
    assert "держит ладонь" not in reply.lower()


def test_rest_stripe_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Придержи ладонь на полоске после полудня")
    assert "полоск" in reply.lower()
    assert "костяш" not in reply.lower()


def test_sweep_crumb_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Смахни крошку после полудня")
    assert "крош" in reply.lower() or "пыльц" in reply.lower()
    assert "костяш" not in reply.lower()
