"""Тёплая складка ремня утром после ночного дыхания."""

from dragonforge import Character


def test_pat_fold_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("поглаживает тёплую складку ремня утром", 0.0)
    reply = dragon.pat_fold("тёплая складка ремня утром")
    after = dragon.soul.habits["поглаживает тёплую складку ремня утром"]
    assert after > before
    assert "складк" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_pat_fold_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("согревает подвёрнутый ремень к вечеру", 0.4)
    dragon.pat_fold()
    assert dragon.soul.habits["согревает подвёрнутый ремень к вечеру"] > 0.4


def test_pat_fold_is_remembered():
    dragon = Character(name="Грок")
    dragon.pat_fold("тёплая складка ремня над рекой утром")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "складк" in blob
    assert "рек" in blob


def test_talk_about_pat_fold():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("поглаживает тёплую складку ремня утром", 0.0)
    reply = dragon.talk("Погладь тёплую складку утром, подворот не трогай")
    after = dragon.soul.habits["поглаживает тёплую складку ремня утром"]
    assert after > before
    assert "складк" in reply.lower()
    assert "седл" in reply.lower()


def test_warm_strap_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Согрей подвёрнутый ремень, чтобы не стыл")
    assert "ремень" in reply.lower()
    assert "поглаживает тёплую складку" not in reply.lower()
