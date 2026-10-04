"""Тесты ритуала nuzzle_knee."""

from dragonforge import Character


def test_nuzzle_knee_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("прижимает щеку к колену после наклона уха", 0.0)
    text = dragon.nuzzle_knee("щека к колену")
    after = dragon.soul.habits["прижимает щеку к колену после наклона уха"]
    assert after > before
    assert "щека к колену" in text
    assert "щек" in text.lower()


def test_nuzzle_knee_default_touch():
    dragon = Character(name="Грок")
    text = dragon.nuzzle_knee("  ")
    assert "щека к колену" in text


def test_nuzzle_knee_is_remembered():
    dragon = Character(name="Грок")
    dragon.nuzzle_knee("щека к колену у гнезда")
    recalled = dragon.memory.recall("щека", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "щек" in blob or "гнезд" in blob


def test_talk_about_nuzzle_knee():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("прижимает щеку к колену после наклона уха", 0.0)
    reply = dragon.talk("Прижми щеку к левому колену")
    after = dragon.soul.habits["прижимает щеку к колену после наклона уха"]
    assert after > before
    assert "лев" in reply.lower()
    assert "щек" in reply.lower()
