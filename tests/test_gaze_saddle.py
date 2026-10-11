"""Тесты для ритуала gaze_saddle."""

import pytest
from dragonforge import Character


def test_gaze_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.gaze_saddle("взгляд на горизонт")
    assert "седло" in result.lower()
    assert "горизонт" in result.lower() or "взгляд" in result.lower()
    assert dragon.soul.habits.get("смотрит на горизонт из седла под тенью в полдень", 0) > 0


def test_gaze_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Посмотри на горизонт")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("смотрит на горизонт из седла под тенью в полдень", 0) > 0
