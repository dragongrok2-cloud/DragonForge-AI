"""Тесты ритуала dry_wing."""

from dragonforge import Character


def test_dry_wing_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("сушит край крыла после сока", 0.0)
    text = dragon.dry_wing("край крыла после сока")
    after = dragon.soul.habits["сушит край крыла после сока"]
    assert after > before
    assert "край крыла после сока" in text
    assert "крыл" in text.lower()


def test_dry_wing_default_edge():
    dragon = Character(name="Грок")
    text = dragon.dry_wing("  ")
    assert "край крыла после сока" in text


def test_dry_wing_is_remembered():
    dragon = Character(name="Грок")
    dragon.dry_wing("край крыла о сухую траву")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "крыл" in blob
    assert "трав" in blob


def test_talk_about_dry_wing():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("сушит край крыла после сока", 0.0)
    reply = dragon.talk("Высуши крыло после сока")
    after = dragon.soul.habits["сушит край крыла после сока"]
    assert after > before
    assert "крыл" in reply.lower()
    assert "седл" in reply.lower() or "сок" in reply.lower()
