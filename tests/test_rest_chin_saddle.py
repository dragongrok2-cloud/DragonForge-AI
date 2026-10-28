"""Тесты для ритуала rest_chin_saddle."""

import pytest
from dragonforge import Character


def test_rest_chin_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.rest_chin_saddle("тихое опирание подбородком")
    assert "седло" in result.lower()
    assert "подбород" in result.lower()
    assert dragon.soul.habits.get("тихо опирается подбородком в седле под тенью к вечеру", 0) > 0


def test_rest_chin_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Опрись подбородком в седле")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо опирается подбородком в седле под тенью к вечеру", 0) > 0
