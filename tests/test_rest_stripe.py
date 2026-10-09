"""Ладонь на светлой полоске после полудня 9 октября."""

from dragonforge import Character


def test_rest_stripe_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("держит ладонь на светлой полоске после полудня", 0.0)
    reply = dragon.rest_stripe("ладонь на светлой полоске после полудня")
    after = dragon.soul.habits["держит ладонь на светлой полоске после полудня"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_rest_stripe_keeps_sweep_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("смахивает крошку с полоски солнца после полудня", 0.4)
    dragon.rest_stripe()
    assert dragon.soul.habits["смахивает крошку с полоски солнца после полудня"] > 0.4


def test_rest_stripe_is_remembered():
    dragon = Character(name="Грок")
    dragon.rest_stripe("ладонь на светлой полоске над рекой после полудня")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "полоск" in blob
    assert "рек" in blob


def test_talk_about_rest_stripe():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("держит ладонь на светлой полоске после полудня", 0.0)
    reply = dragon.talk("Придержи ладонь на полоске после полудня")
    after = dragon.soul.habits["держит ладонь на светлой полоске после полудня"]
    assert after > before
    assert "седл" in reply.lower()
    assert "смахивает крошку" not in reply.lower()


def test_sweep_crumb_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Смахни крошку после полудня")
    assert "крош" in reply.lower() or "пыльц" in reply.lower()
    assert "держит ладонь" not in reply.lower()


def test_share_crumb_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Поделись крошкой в полдень")
    assert "крош" in reply.lower() or "полоск" in reply.lower()
    assert "держит ладонь" not in reply.lower()
