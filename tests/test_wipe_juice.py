"""Тесты ритуала wipe_juice."""

from dragonforge import Character


def test_wipe_juice_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("вытирает сок с луки после яблока", 0.0)
    text = dragon.wipe_juice("сок с луки после яблока")
    after = dragon.soul.habits["вытирает сок с луки после яблока"]
    assert after > before
    assert "сок с луки после яблока" in text
    assert "сок" in text.lower()


def test_wipe_juice_default_spot():
    dragon = Character(name="Грок")
    text = dragon.wipe_juice("  ")
    assert "сок с луки после яблока" in text


def test_wipe_juice_is_remembered():
    dragon = Character(name="Грок")
    dragon.wipe_juice("сок, снятый крылом")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "сок" in blob
    assert "крылом" in blob


def test_talk_about_wipe_juice():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("вытирает сок с луки после яблока", 0.0)
    reply = dragon.talk("Вытри сок с луки")
    after = dragon.soul.habits["вытирает сок с луки после яблока"]
    assert after > before
    assert "сок" in reply.lower()
    assert "седл" in reply.lower() or "луки" in reply.lower()
