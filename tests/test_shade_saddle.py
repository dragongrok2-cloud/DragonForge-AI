"""Тесты для ритуала shade_saddle."""

import pytest
from dragonforge import Character


def test_shade_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.shade_saddle("седло под крылом")
    assert "седло" in result.lower()
    assert "тен" in result.lower() or "крыл" in result.lower()
    assert dragon.soul.habits.get("даёт тень крылом в седле в полдень", 0) > 0


def test_shade_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Дай тень в седле")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("даёт тень крылом в седле в полдень", 0) > 0
