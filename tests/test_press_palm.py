"""Тесты ритуала press_palm."""

from dragonforge import Character


def test_press_palm_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("прижимает ладонь после накрытия", 0.0)
    text = dragon.press_palm("мягкое нажатие после накрытия")
    after = dragon.soul.habits["прижимает ладонь после накрытия"]
    assert after > before
    assert "мягкое нажатие после накрытия" in text
    assert "ладон" in text.lower()
    assert "седл" in text.lower()


def test_press_palm_default_place():
    dragon = Character(name="Грок")
    text = dragon.press_palm("  ")
    assert "мягкое нажатие после накрытия" in text


def test_press_palm_is_remembered():
    dragon = Character(name="Грок")
    dragon.press_palm("нажатие у луки")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "ладон" in blob
    assert "нажат" in blob or "лук" in blob


def test_talk_about_press_palm():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("прижимает ладонь после накрытия", 0.0)
    reply = dragon.talk("Прижми ладонь один раз")
    after = dragon.soul.habits["прижимает ладонь после накрытия"]
    assert after > before
    assert "ладон" in reply.lower() or "нажат" in reply.lower()
    assert "седл" in reply.lower()
