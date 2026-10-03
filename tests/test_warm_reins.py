"""Тесты послеполуденного прогрева поводьев."""

from dragonforge import Character


def test_warm_reins_strengthens_habit_and_joy():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("прогревает поводья после полудня", 0.0)
    joy_before = dragon.soul.emotional_state.get("joy", 0.5)
    text = dragon.warm_reins("обе руки")
    after = dragon.soul.habits["прогревает поводья после полудня"]
    assert after > before
    assert dragon.soul.emotional_state["joy"] > joy_before
    assert "повод" in text.lower()
    assert "обе руки" in text


def test_warm_reins_is_remembered():
    dragon = Character(name="Грок")
    dragon.warm_reins("левая рука")
    recalled = dragon.memory.recall("поводья", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "повод" in blob or "седл" in blob


def test_talk_about_reins_warms():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("прогревает поводья после полудня", 0.0)
    reply = dragon.talk("Прогрей поводья для левой руки")
    after = dragon.soul.habits["прогревает поводья после полудня"]
    assert after > before
    assert "повод" in reply.lower()
    assert "левая" in reply.lower()
