"""Тесты для ритуала bask_saddle."""

import pytest
from dragonforge import Character


def test_bask_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.bask_saddle("седло под солнцем")
    assert "седло" in result.lower()
    assert "солнц" in result.lower() or "гре" in result.lower()
    assert dragon.soul.habits.get("греется в седле под утренним солнцем", 0) > 0


def test_bask_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Погрейся в седле")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("греется в седле под утренним солнцем", 0) > 0
