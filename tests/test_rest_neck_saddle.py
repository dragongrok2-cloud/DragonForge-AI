"""Тесты для ритуала rest_neck_saddle."""

import pytest
from dragonforge import Character


def test_rest_neck_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.rest_neck_saddle("тихое прижатие шеи")
    assert "седло" in result.lower()
    assert "шея" in result.lower() or "шеей" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается шеей к седлу под тенью к вечеру", 0) > 0


def test_rest_neck_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Прижмись шеей к седлу")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается шеей к седлу под тенью к вечеру", 0) > 0
