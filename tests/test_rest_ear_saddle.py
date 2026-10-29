"""Тесты для ритуала rest_ear_saddle."""

import pytest
from dragonforge import Character


def test_rest_ear_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.rest_ear_saddle("тихое прижатие уха")
    assert "седло" in result.lower()
    assert "ух" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается ухом к седлу под тенью к вечеру", 0) > 0


def test_rest_ear_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Прижмись ухом к седлу")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается ухом к седлу под тенью к вечеру", 0) > 0
