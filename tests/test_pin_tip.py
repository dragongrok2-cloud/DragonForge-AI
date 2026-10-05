"""Тесты ритуала pin_tip."""

from dragonforge import Character


def test_pin_tip_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("закрепляет кончик крыла после подгиба", 0.0)
    text = dragon.pin_tip("кончик у луки после подгиба")
    after = dragon.soul.habits["закрепляет кончик крыла после подгиба"]
    assert after > before
    assert "кончик у луки после подгиба" in text
    assert "крыл" in text.lower()
    assert "седл" in text.lower()


def test_pin_tip_default_place():
    dragon = Character(name="Грок")
    text = dragon.pin_tip("  ")
    assert "кончик у луки после подгиба" in text


def test_pin_tip_is_remembered():
    dragon = Character(name="Грок")
    dragon.pin_tip("кончик под мягкой чешуйкой")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "кончик" in blob
    assert "лук" in blob or "чешу" in blob


def test_talk_about_pin_tip():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("закрепляет кончик крыла после подгиба", 0.0)
    reply = dragon.talk("Закрепи кончик крыла")
    after = dragon.soul.habits["закрепляет кончик крыла после подгиба"]
    assert after > before
    assert "кончик" in reply.lower()
    assert "седл" in reply.lower() or "лук" in reply.lower()
