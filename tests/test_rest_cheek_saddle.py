"""Тесты для ритуала rest_cheek_saddle."""

import pytest
from dragonforge import Character


def test_rest_cheek_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.rest_cheek_saddle("тихое прижатие щеки")
    assert "седло" in result.lower()
    assert "щек" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается щекой к седлу под тенью к вечеру", 0) > 0


def test_rest_cheek_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Прижмись щекой к седлу")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо прижимается щекой к седлу под тенью к вечеру", 0) > 0
