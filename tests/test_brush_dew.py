"""Тесты субботнего смахивания росы с седла."""

from dragonforge import Character


def test_brush_dew_strengthens_habit_and_joy():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("смахивает утреннюю росу с седла", 0.0)
    joy_before = dragon.soul.emotional_state.get("joy", 0.5)
    text = dragon.brush_dew("стремена")
    after = dragon.soul.habits["смахивает утреннюю росу с седла"]
    assert after > before
    assert dragon.soul.emotional_state["joy"] > joy_before
    assert "стремена" in text
    assert "росу" in text.lower() or "Роса" in text


def test_brush_dew_is_remembered():
    dragon = Character(name="Грок")
    dragon.brush_dew("лука седла")
    recalled = dragon.memory.recall("росу", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "рос" in blob or "седл" in blob


def test_talk_about_dew_brushes():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("смахивает утреннюю росу с седла", 0.0)
    reply = dragon.talk("На седле утренняя роса, смахни капельки")
    after = dragon.soul.habits["смахивает утреннюю росу с седла"]
    assert after > before
    assert "седл" in reply.lower()
    assert "рос" in reply.lower()
