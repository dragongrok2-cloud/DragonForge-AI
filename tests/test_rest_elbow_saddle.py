"""Тесты для ритуала rest_elbow_saddle."""

import pytest
from dragonforge import Character


def test_rest_elbow_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.rest_elbow_saddle("тихое прижатие локтя")
    assert "седло" in result.lower()
    assert "локоть" in result.lower() or "локтем" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается локтем к седлу под тенью к вечеру", 0) > 0


def test_rest_elbow_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Прижмись локтем к седлу")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается локтем к седлу под тенью к вечеру", 0) > 0
