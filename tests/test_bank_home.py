"""Тесты вечернего разворота к гнезду."""

from dragonforge import Character


def test_bank_home_strengthens_habit_and_trust():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("разворачивается к гнезду к ночи", 0.0)
    trust_before = dragon.soul.emotional_state.get("trust", 0.5)
    text = dragon.bank_home("пещера на утёсе")
    after = dragon.soul.habits["разворачивается к гнезду к ночи"]
    assert after > before
    assert dragon.soul.emotional_state["trust"] > trust_before
    assert "пещера на утёсе" in text
    assert "Гнездо ждёт" in text


def test_bank_home_is_remembered():
    dragon = Character(name="Грок")
    dragon.bank_home("гнездо у реки")
    recalled = dragon.memory.recall("гнездо", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "гнезд" in blob or "реки" in blob


def test_talk_about_home_banks():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("разворачивается к гнезду к ночи", 0.0)
    reply = dragon.talk("Пора домой, к гнезду")
    after = dragon.soul.habits["разворачивается к гнезду к ночи"]
    assert after > before
    assert "гнездо" in reply.lower()
    assert "седло" in reply.lower()
