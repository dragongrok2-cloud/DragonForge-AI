"""Тесты ритуала blink_slow."""

from dragonforge import Character


def test_blink_slow_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("медленно моргает после морды на луке", 0.0)
    text = dragon.blink_slow("медленное моргание")
    after = dragon.soul.habits["медленно моргает после морды на луке"]
    assert after > before
    assert "медленное моргание" in text
    assert "морга" in text.lower()


def test_blink_slow_default_sign():
    dragon = Character(name="Грок")
    text = dragon.blink_slow("  ")
    assert "медленное моргание" in text


def test_blink_slow_is_remembered():
    dragon = Character(name="Грок")
    dragon.blink_slow("моргание левым глазом")
    recalled = dragon.memory.recall("моргнул", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "морг" in blob or "лев" in blob


def test_talk_about_slow_blink():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("медленно моргает после морды на луке", 0.0)
    reply = dragon.talk("Моргни левым глазом")
    after = dragon.soul.habits["медленно моргает после морды на луке"]
    assert after > before
    assert "морга" in reply.lower()
    assert "лев" in reply.lower()
