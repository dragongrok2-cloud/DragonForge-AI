"""Пальцы в полоске солнца после полудня 9 октября."""

from dragonforge import Character


def test_curl_fingers_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("сгибает пальцы в полоске солнца после полудня", 0.0)
    reply = dragon.curl_fingers("пальцы в полоске солнца после полудня")
    after = dragon.soul.habits["сгибает пальцы в полоске солнца после полудня"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "сгиб" in reply.lower()


def test_curl_fingers_keeps_shift_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("сдвигает полоску солнца на костяшки после полудня", 0.4)
    dragon.curl_fingers()
    assert dragon.soul.habits["сдвигает полоску солнца на костяшки после полудня"] > 0.4


def test_curl_fingers_is_remembered():
    dragon = Character(name="Грок")
    dragon.curl_fingers("пальцы в полоске солнца над рекой после полудня")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "пальц" in blob or "сгиб" in blob
    assert "рек" in blob


def test_talk_about_curl_fingers():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("сгибает пальцы в полоске солнца после полудня", 0.0)
    reply = dragon.talk("Согни пальцы в полоске после полудня")
    after = dragon.soul.habits["сгибает пальцы в полоске солнца после полудня"]
    assert after > before
    assert "седл" in reply.lower()
    assert "сдвигает полоску" not in reply.lower()


def test_shift_stripe_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Сдвинь полоску на костяшки после полудня")
    assert "костяш" in reply.lower()
    assert "сгиб" not in reply.lower()


def test_rest_stripe_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Придержи ладонь на полоске после полудня")
    assert "полоск" in reply.lower()
    assert "сгиб" not in reply.lower()
