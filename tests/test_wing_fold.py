"""Тесты послеполётного складывания крыльев."""

from dragonforge import Character


def test_fold_wings_strengthens_habit_and_rests():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("складывает крылья после полёта", 0.0)
    energy_before = dragon.soul.emotional_state["energy"]
    text = dragon.fold_wings()
    after = dragon.soul.habits["складывает крылья после полёта"]
    assert after > before
    assert dragon.soul.emotional_state["energy"] < energy_before
    assert "Крылья сложены" in text
    assert "седло" in text.lower()


def test_fold_wings_is_remembered():
    dragon = Character(name="Грок")
    dragon.fold_wings()
    recalled = dragon.memory.recall("сложил крылья", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "крыл" in blob


def test_talk_asks_to_fold_wings():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("складывает крылья после полёта", 0.0)
    reply = dragon.talk("Сложи крылья после полёта")
    after = dragon.soul.habits["складывает крылья после полёта"]
    assert after > before
    assert "сложены" in reply.lower()
