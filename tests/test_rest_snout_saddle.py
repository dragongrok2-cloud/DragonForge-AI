"""Тесты для ритуала rest_snout_saddle."""

import pytest
from dragonforge import Character


def test_rest_snout_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.rest_snout_saddle("тихое прижатие носа")
    assert "седло" in result.lower()
    assert "нос" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается носом к седлу под тенью к вечеру", 0) > 0


def test_rest_snout_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Прижмись носом к седлу")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается носом к седлу под тенью к вечеру", 0) > 0
