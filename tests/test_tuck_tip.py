"""Тесты ритуала tuck_tip."""

from dragonforge import Character


def test_tuck_tip_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("подгибает кончик крыла после сушки", 0.0)
    text = dragon.tuck_tip("кончик крыла после сушки")
    after = dragon.soul.habits["подгибает кончик крыла после сушки"]
    assert after > before
    assert "кончик крыла после сушки" in text
    assert "крыл" in text.lower()


def test_tuck_tip_default_tip():
    dragon = Character(name="Грок")
    text = dragon.tuck_tip("  ")
    assert "кончик крыла после сушки" in text


def test_tuck_tip_is_remembered():
    dragon = Character(name="Грок")
    dragon.tuck_tip("кончик крыла к луке")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "кончик" in blob
    assert "лук" in blob


def test_talk_about_tuck_tip():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("подгибает кончик крыла после сушки", 0.0)
    reply = dragon.talk("Подогни кончик крыла")
    after = dragon.soul.habits["подгибает кончик крыла после сушки"]
    assert after > before
    assert "кончик" in reply.lower() or "крыл" in reply.lower()
    assert "седл" in reply.lower() or "лук" in reply.lower()
