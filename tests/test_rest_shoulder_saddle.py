"""Тесты для ритуала rest_shoulder_saddle."""

import pytest
from dragonforge import Character


def test_rest_shoulder_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.rest_shoulder_saddle("тихое прижатие плеча")
    assert "седло" in result.lower()
    assert "плечо" in result.lower() or "плечом" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается плечом к седлу под тенью к вечеру", 0) > 0


def test_rest_shoulder_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Прижмись плечом к седлу")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается плечом к седлу под тенью к вечеру", 0) > 0
