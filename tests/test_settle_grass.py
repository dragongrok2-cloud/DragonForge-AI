"""Тесты ритуала settle_grass."""

from dragonforge import Character


def test_settle_grass_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("опускается на траву после короткого круга", 0.0)
    text = dragon.settle_grass("мягкая трава у луга")
    after = dragon.soul.habits["опускается на траву после короткого круга"]
    assert after > before
    assert "мягкая трава у луга" in text
    assert "трав" in text.lower()


def test_settle_grass_default_patch():
    dragon = Character(name="Грок")
    text = dragon.settle_grass("  ")
    assert "мягкая трава у луга" in text


def test_settle_grass_is_remembered():
    dragon = Character(name="Грок")
    dragon.settle_grass("трава у гнезда")
    recalled = dragon.memory.recall("трава", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "трав" in blob or "гнезд" in blob


def test_talk_about_settle_grass():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("опускается на траву после короткого круга", 0.0)
    reply = dragon.talk("Опустись на траву под хребтом")
    after = dragon.soul.habits["опускается на траву после короткого круга"]
    assert after > before
    assert "хреб" in reply.lower()
    assert "трав" in reply.lower()
