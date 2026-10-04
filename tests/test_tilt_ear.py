"""Тесты ритуала tilt_ear."""

from dragonforge import Character


def test_tilt_ear_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("наклоняет ухо к седлу после низкого гула", 0.0)
    text = dragon.tilt_ear("ухо к седлу")
    after = dragon.soul.habits["наклоняет ухо к седлу после низкого гула"]
    assert after > before
    assert "ухо к седлу" in text
    assert "ухо" in text.lower()


def test_tilt_ear_default_side():
    dragon = Character(name="Грок")
    text = dragon.tilt_ear("  ")
    assert "ухо к седлу" in text


def test_tilt_ear_is_remembered():
    dragon = Character(name="Грок")
    dragon.tilt_ear("ухо к седлу у гнезда")
    recalled = dragon.memory.recall("ухо", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "ухо" in blob or "гнезд" in blob


def test_talk_about_tilt_ear():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("наклоняет ухо к седлу после низкого гула", 0.0)
    reply = dragon.talk("Наклони левое ухо к седлу")
    after = dragon.soul.habits["наклоняет ухо к седлу после низкого гула"]
    assert after > before
    assert "лев" in reply.lower()
    assert "ухо" in reply.lower()
