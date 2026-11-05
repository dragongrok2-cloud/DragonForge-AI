"""Тест ритуала rest_iris_saddle."""

from dragonforge import Character


def test_rest_iris_saddle_strengthens_habit_and_emotions():
    dragon = Character(name="Тестовый")
    initial_joy = dragon.soul.emotional_state.get("joy", 0.5)
    initial_trust = dragon.soul.emotional_state.get("trust", 0.5)

    result = dragon.rest_iris_saddle("тихая тень")

    assert "радужк" in result.lower() or "iris" in result.lower() or "седло" in result.lower()
    assert dragon.soul.emotional_state["joy"] > initial_joy
    assert dragon.soul.emotional_state["trust"] > initial_trust
    assert any("радужк" in k for k in dragon.soul.habits)
    assert dragon.memory.memories  # что-то запомнилось
