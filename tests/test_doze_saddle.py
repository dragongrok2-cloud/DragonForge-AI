"""Тесты для ритуала doze_saddle."""

import pytest
from dragonforge import Character


def test_doze_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.doze_saddle("тихое дремание")
    assert "седло" in result.lower()
    assert "дрем" in result.lower()
    assert dragon.soul.habits.get("тихо дремлет в седле под тенью к вечеру", 0) > 0


def test_doze_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Дремли в седле")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо дремлет в седле под тенью к вечеру", 0) > 0
