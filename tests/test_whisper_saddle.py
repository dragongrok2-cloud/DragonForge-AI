"""Тесты для ритуала whisper_saddle."""

import pytest
from dragonforge import Character


def test_whisper_saddle_basic():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.whisper_saddle("тихий шёпот")
    assert "седло" in result.lower()
    assert "шеп" in result.lower() or "шёп" in result.lower()
    assert dragon.soul.habits.get("тихо шепчет седлу под тенью к вечеру", 0) > 0


def test_whisper_saddle_talk_trigger():
    dragon = Character(name="ТестДракон", species="Дракон")
    result = dragon.talk("Шепни седлу")
    assert "седло" in result.lower()
    assert dragon.soul.habits.get("тихо шепчет седлу под тенью к вечеру", 0) > 0
