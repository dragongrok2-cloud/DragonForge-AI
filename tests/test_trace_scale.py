"""Тесты для метода trace_scale."""
import pytest
from dragonforge.core.character import Character

def test_trace_scale_strengthens_habit():
    dragon = Character(name="Тест")
    before = dragon.soul.habits.get("обводит чешуйку после подъёма ладони", 0.0)
    result = dragon.trace_scale()
    after = dragon.soul.habits.get("обводит чешуйку после подъёма ладони", 0.0)
    assert after > before
    assert "чешуйк" in result.lower()
    assert "привычка" in result.lower()

def test_trace_scale_remembers():
    dragon = Character(name="Тест")
    dragon.trace_scale("особая чешуйка")
    memories = dragon.memory.recall("чешуйк")
    assert any("чешуйк" in str(m).lower() for m in memories)
