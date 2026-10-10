"""Погладить луку утром 10 октября после тепла."""

from dragonforge import Character


def test_pat_pommel_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("гладит луку утром после тепла", 0.0)
    reply = dragon.pat_pommel("луку утром после тепла")
    after = dragon.soul.habits["гладит луку утром после тепла"]
    assert after > before
    assert "лук" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "глад" in reply.lower() or "ладон" in reply.lower()


def test_pat_pommel_keeps_warmth_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("кладёт тепло сгиба на луку к вечеру", 0.4)
    dragon.pat_pommel()
    assert dragon.soul.habits["кладёт тепло сгиба на луку к вечеру"] > 0.4


def test_pat_pommel_is_remembered():
    dragon = Character(name="Грок")
    dragon.pat_pommel("луку над рекой утром после тепла")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "лук" in blob or "глад" in blob
    assert "рек" in blob


def test_talk_about_pat_pommel():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("гладит луку утром после тепла", 0.0)
    reply = dragon.talk("Погладь луку утром")
    after = dragon.soul.habits["гладит луку утром после тепла"]
    assert after > before
    assert "седл" in reply.lower()
    assert "кладёт тепло" not in reply.lower()


def test_lay_warmth_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Положи тепло на луку к вечеру")
    assert "тепло" in reply.lower()
    assert "гладит луку" not in reply.lower()


def test_ease_fold_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Разжми сгиб к вечеру")
    assert "сгиб" in reply.lower()
    assert "гладит луку" not in reply.lower()
