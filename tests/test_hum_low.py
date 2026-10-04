"""Тесты ритуала hum_low."""

from dragonforge import Character


def test_hum_low_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("гудит низко после приседа на траву", 0.0)
    text = dragon.hum_low("тихий гул над травой")
    after = dragon.soul.habits["гудит низко после приседа на траву"]
    assert after > before
    assert "тихий гул над травой" in text
    assert "гул" in text.lower()


def test_hum_low_default_note():
    dragon = Character(name="Грок")
    text = dragon.hum_low("  ")
    assert "тихий гул над травой" in text


def test_hum_low_is_remembered():
    dragon = Character(name="Грок")
    dragon.hum_low("тихий гул у гнезда")
    recalled = dragon.memory.recall("гул", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "гул" in blob or "гнезд" in blob


def test_talk_about_hum_low():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("гудит низко после приседа на траву", 0.0)
    reply = dragon.talk("Погуди тихо по ремням седла")
    after = dragon.soul.habits["гудит низко после приседа на траву"]
    assert after > before
    assert "седл" in reply.lower()
    assert "гул" in reply.lower()
