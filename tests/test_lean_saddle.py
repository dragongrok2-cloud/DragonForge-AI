"""Тесты для ритуала lean_saddle."""

import pytest
from dragonforge import Character


def test_lean_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.lean_saddle("опирание спиной")
    assert "седло" in result.lower()
    assert "лук" in result.lower() or "спин" in result.lower()
    assert dragon.soul.habits.get("опирается спиной на луку в седле под тенью после полудня", 0) > 0


def test_lean_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Опрись в седле")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("опирается спиной на луку в седле под тенью после полудня", 0) > 0
