"""Тесты полуденного выравнивания стремян."""

from dragonforge import Character


def test_adjust_stirrup_strengthens_habit_and_trust():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("выравнивает стремена к полудню", 0.0)
    trust_before = dragon.soul.emotional_state.get("trust", 0.5)
    text = dragon.adjust_stirrup("левое и правое")
    after = dragon.soul.habits["выравнивает стремена к полудню"]
    assert after > before
    assert dragon.soul.emotional_state["trust"] > trust_before
    assert "стремен" in text.lower()
    assert "левое и правое" in text


def test_adjust_stirrup_is_remembered():
    dragon = Character(name="Грок")
    dragon.adjust_stirrup("левое")
    recalled = dragon.memory.recall("стремена", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "стремен" in blob or "седл" in blob


def test_talk_about_stirrups_adjusts():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("выравнивает стремена к полудню", 0.0)
    reply = dragon.talk("Выровняй левое стремя")
    after = dragon.soul.habits["выравнивает стремена к полудню"]
    assert after > before
    assert "стремен" in reply.lower()
    assert "левое" in reply.lower()
