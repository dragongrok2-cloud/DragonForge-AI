"""Тесты для ритуала murmur_saddle."""

import pytest
from dragonforge import Character


def test_murmur_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.murmur_saddle("тихое бормотание")
    assert "седло" in result.lower()
    assert "бормоч" in result.lower()
    assert dragon.soul.habits.get("тихо бормочет в седле под тенью к вечеру", 0) > 0


def test_murmur_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Бормочи в седле")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо бормочет в седле под тенью к вечеру", 0) > 0
