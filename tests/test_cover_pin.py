"""Тесты ритуала cover_pin."""

from dragonforge import Character


def test_cover_pin_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("накрывает чешуйку после закрепления", 0.0)
    text = dragon.cover_pin("ладонь на чешуйке после закрепления")
    after = dragon.soul.habits["накрывает чешуйку после закрепления"]
    assert after > before
    assert "ладонь на чешуйке после закрепления" in text
    assert "чешу" in text.lower()
    assert "седл" in text.lower()


def test_cover_pin_default_place():
    dragon = Character(name="Грок")
    text = dragon.cover_pin("  ")
    assert "ладонь на чешуйке после закрепления" in text


def test_cover_pin_is_remembered():
    dragon = Character(name="Грок")
    dragon.cover_pin("ладонь на чешуйке у луки")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "чешу" in blob
    assert "ладон" in blob or "лук" in blob


def test_talk_about_cover_pin():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("накрывает чешуйку после закрепления", 0.0)
    reply = dragon.talk("Накрой чешуйку ладонью")
    after = dragon.soul.habits["накрывает чешуйку после закрепления"]
    assert after > before
    assert "чешу" in reply.lower()
    assert "седл" in reply.lower() or "ладон" in reply.lower()
