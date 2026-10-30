"""Тест ритуала rest_knee_saddle."""

from dragonforge import Character


def test_rest_knee_saddle_strengthens_habit():
    dragon = Character(name="Тест")
    before = dragon.soul.habits.get("тихо прижимается коленом к седлу под тенью к вечеру", 0.0)
    result = dragon.rest_knee_saddle("тест")
    after = dragon.soul.habits.get("тихо прижимается коленом к седлу под тенью к вечеру", 0.0)
    assert after > before
    assert "коленом" in result.lower()
    assert "седло" in result.lower()


def test_talk_triggers_knee():
    dragon = Character(name="Тест")
    result = dragon.talk("прижмись коленом к седлу")
    assert "коленом" in result.lower()
