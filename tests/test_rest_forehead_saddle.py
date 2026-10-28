"""Тесты для ритуала rest_forehead_saddle."""

import pytest
from dragonforge import Character


def test_rest_forehead_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.rest_forehead_saddle("тихое прижатие лба")
    assert "седло" in result.lower()
    assert "лб" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается лбом к седлу под тенью к вечеру", 0) > 0


def test_rest_forehead_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Прижмись лбом к седлу")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается лбом к седлу под тенью к вечеру", 0) > 0
