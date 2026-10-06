"""Тесты ритуала blot_scale."""

from dragonforge import Character


def test_blot_scale_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("промокает чешуйку после ладони", 0.0)
    text = dragon.blot_scale("роса с чешуйки после ладони")
    after = dragon.soul.habits["промокает чешуйку после ладони"]
    assert after > before
    assert "роса с чешуйки после ладони" in text
    assert "чешу" in text.lower()
    assert "седл" in text.lower()


def test_blot_scale_default_place():
    dragon = Character(name="Грок")
    text = dragon.blot_scale("  ")
    assert "роса с чешуйки после ладони" in text


def test_blot_scale_is_remembered():
    dragon = Character(name="Грок")
    dragon.blot_scale("роса с чешуйки у луки")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "чешу" in blob
    assert "рос" in blob or "ладон" in blob


def test_talk_about_blot_scale():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("промокает чешуйку после ладони", 0.0)
    reply = dragon.talk("Промокни чешуйку после ладони")
    after = dragon.soul.habits["промокает чешуйку после ладони"]
    assert after > before
    assert "чешу" in reply.lower()
    assert "седл" in reply.lower() or "рос" in reply.lower()
