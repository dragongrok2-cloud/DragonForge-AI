"""Тесты пятничного ритуала: тёплый термос в седле."""

from dragonforge import Character


def test_pour_thermos_strengthens_habit_and_joy():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("делится тёплым термосом в седле", 0.0)
    joy_before = dragon.soul.emotional_state["joy"]
    text = dragon.pour_thermos("какао")
    after = dragon.soul.habits["делится тёплым термосом в седле"]
    assert after > before
    assert dragon.soul.emotional_state["joy"] > joy_before
    assert "какао" in text.lower()
    assert "седле" in text.lower() or "седло" in text.lower()


def test_pour_thermos_is_remembered():
    dragon = Character(name="Грок")
    dragon.pour_thermos("чай")
    recalled = dragon.memory.recall("разлил", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "термос" in blob or "чай" in blob


def test_talk_asks_for_thermos():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("делится тёплым термосом в седле", 0.0)
    reply = dragon.talk("Налей чай из термоса")
    after = dragon.soul.habits["делится тёплым термосом в седле"]
    assert after > before
    assert "чай" in reply.lower()
