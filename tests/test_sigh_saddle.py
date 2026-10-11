"""Тесты для ритуала sigh_saddle."""

import pytest
from dragonforge import Character


def test_sigh_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.sigh_saddle("тихий вздох")
    assert "седло" in result.lower()
    assert "вздох" in result.lower()
    assert dragon.soul.habits.get("тихо вздыхает в седле под тенью после полудня", 0) > 0


def test_sigh_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Вздохни в седле")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо вздыхает в седле под тенью после полудня", 0) > 0
