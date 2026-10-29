"""Тесты для ритуала rest_jaw_saddle."""

import pytest
from dragonforge import Character


def test_rest_jaw_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.rest_jaw_saddle("тихое прижатие челюсти")
    assert "седло" in result.lower()
    assert "челюст" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается челюстью к седлу под тенью к вечеру", 0) > 0


def test_rest_jaw_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Прижмись челюстью к седлу")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается челюстью к седлу под тенью к вечеру", 0) > 0
