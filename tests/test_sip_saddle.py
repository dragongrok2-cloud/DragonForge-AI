"""Тесты для ритуала sip_saddle."""

import pytest
from dragonforge import Character


def test_sip_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.sip_saddle("глоток в седле")
    assert "седло" in result.lower()
    assert "глоток" in result.lower() or "термос" in result.lower()
    assert dragon.soul.habits.get("делает глоток в седле под тенью в полдень", 0) > 0


def test_sip_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Сделай глоток в седле")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("делает глоток в седле под тенью в полдень", 0) > 0
