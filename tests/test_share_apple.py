"""Тесты ритуала share_apple."""

from dragonforge import Character


def test_share_apple_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("делится яблоком после гладкой луки", 0.0)
    text = dragon.share_apple("кислое яблоко из седельной сумки")
    after = dragon.soul.habits["делится яблоком после гладкой луки"]
    assert after > before
    assert "кислое яблоко из седельной сумки" in text
    assert "яблок" in text.lower()


def test_share_apple_default_fruit():
    dragon = Character(name="Грок")
    text = dragon.share_apple("  ")
    assert "кислое яблоко из седельной сумки" in text


def test_share_apple_is_remembered():
    dragon = Character(name="Грок")
    dragon.share_apple("половинка яблока")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "яблок" in blob
    assert "половинка" in blob


def test_talk_about_share_apple():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("делится яблоком после гладкой луки", 0.0)
    reply = dragon.talk("Поделись яблоком после луки")
    after = dragon.soul.habits["делится яблоком после гладкой луки"]
    assert after > before
    assert "яблок" in reply.lower()
    assert "седл" in reply.lower()
