"""Тепло сгиба на луке к вечеру 9 октября."""

from dragonforge import Character


def test_lay_warmth_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("кладёт тепло сгиба на луку к вечеру", 0.0)
    reply = dragon.lay_warmth("тепло сгиба на луке к вечеру")
    after = dragon.soul.habits["кладёт тепло сгиба на луку к вечеру"]
    assert after > before
    assert "лук" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "тепло" in reply.lower()


def test_lay_warmth_keeps_ease_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("разжимает сгиб полоски солнца к вечеру", 0.4)
    dragon.lay_warmth()
    assert dragon.soul.habits["разжимает сгиб полоски солнца к вечеру"] > 0.4


def test_lay_warmth_is_remembered():
    dragon = Character(name="Грок")
    dragon.lay_warmth("тепло сгиба на луке над рекой к вечеру")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "тепло" in blob or "лук" in blob
    assert "рек" in blob


def test_talk_about_lay_warmth():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("кладёт тепло сгиба на луку к вечеру", 0.0)
    reply = dragon.talk("Положи тепло на луку к вечеру")
    after = dragon.soul.habits["кладёт тепло сгиба на луку к вечеру"]
    assert after > before
    assert "седл" in reply.lower()
    assert "разжимает сгиб" not in reply.lower()


def test_ease_fold_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Разжми сгиб к вечеру")
    assert "сгиб" in reply.lower()
    assert "кладёт тепло" not in reply.lower()


def test_curl_fingers_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Согни пальцы в полоске после полудня")
    assert "сгиб" in reply.lower()
    assert "кладёт тепло" not in reply.lower()
