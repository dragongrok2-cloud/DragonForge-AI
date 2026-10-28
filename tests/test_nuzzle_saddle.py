"""Тесты для ритуала nuzzle_saddle."""

import pytest
from dragonforge import Character


def test_nuzzle_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.nuzzle_saddle("тихое прижатие")
    assert "седло" in result.lower()
    assert "морд" in result.lower() or "приж" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается мордой к седлу под тенью к вечеру", 0) > 0


def test_nuzzle_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Прижмись к седлу")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается мордой к седлу под тенью к вечеру", 0) > 0
