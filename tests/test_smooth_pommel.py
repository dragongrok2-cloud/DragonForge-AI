"""Тесты ритуала smooth_pommel."""

from dragonforge import Character


def test_smooth_pommel_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("разглаживает луку после кленовых листьев", 0.0)
    text = dragon.smooth_pommel("лука после листьев")
    after = dragon.soul.habits["разглаживает луку после кленовых листьев"]
    assert after > before
    assert "лука после листьев" in text
    assert "лук" in text.lower()


def test_smooth_pommel_default_spot():
    dragon = Character(name="Грок")
    text = dragon.smooth_pommel("  ")
    assert "лука после листьев" in text


def test_smooth_pommel_is_remembered():
    dragon = Character(name="Грок")
    dragon.smooth_pommel("лука над стременем")
    recalled = dragon.memory.recall("луку", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "лук" in blob or "седл" in blob


def test_talk_about_smooth_pommel():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("разглаживает луку после кленовых листьев", 0.0)
    reply = dragon.talk("Разгладь луку после листьев")
    after = dragon.soul.habits["разглаживает луку после кленовых листьев"]
    assert after > before
    assert "лук" in reply.lower()
    assert "седл" in reply.lower()
