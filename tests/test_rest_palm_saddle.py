"""Тест ритуала rest_palm_saddle."""

from dragonforge import Character


def test_rest_palm_saddle_strengthens_habit():
    dragon = Character(name="Тест")
    before = dragon.soul.habits.get("тихо прижимается ладонью к седлу под тенью к вечеру", 0.0)
    result = dragon.rest_palm_saddle("тест")
    after = dragon.soul.habits.get("тихо прижимается ладонью к седлу под тенью к вечеру", 0.0)
    assert after > before
    assert "ладонью" in result.lower()
    assert "седло" in result.lower()


def test_talk_triggers_palm():
    dragon = Character(name="Тест")
    result = dragon.talk("прижмись ладонью к седлу")
    assert "ладонью" in result.lower()
