"""Сгиб полоски солнца к вечеру 9 октября."""

from dragonforge import Character


def test_ease_fold_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("разжимает сгиб полоски солнца к вечеру", 0.0)
    reply = dragon.ease_fold("сгиб полоски солнца к вечеру")
    after = dragon.soul.habits["разжимает сгиб полоски солнца к вечеру"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "тепло" in reply.lower()


def test_ease_fold_keeps_curl_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("сгибает пальцы в полоске солнца после полудня", 0.4)
    dragon.ease_fold()
    assert dragon.soul.habits["сгибает пальцы в полоске солнца после полудня"] > 0.4


def test_ease_fold_is_remembered():
    dragon = Character(name="Грок")
    dragon.ease_fold("сгиб полоски солнца над рекой к вечеру")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "сгиб" in blob or "тепло" in blob
    assert "рек" in blob


def test_talk_about_ease_fold():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("разжимает сгиб полоски солнца к вечеру", 0.0)
    reply = dragon.talk("Разжми сгиб к вечеру")
    after = dragon.soul.habits["разжимает сгиб полоски солнца к вечеру"]
    assert after > before
    assert "седл" in reply.lower()
    assert "сгибает пальцы" not in reply.lower()


def test_curl_fingers_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Согни пальцы в полоске после полудня")
    assert "сгиб" in reply.lower()
    assert "разжимает сгиб" not in reply.lower()


def test_shift_stripe_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Сдвинь полоску на костяшки после полудня")
    assert "костяш" in reply.lower()
    assert "разжимает" not in reply.lower()
