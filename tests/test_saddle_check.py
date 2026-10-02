"""Тесты полуденной проверки седла."""

from dragonforge import Character


def test_check_saddle_strengthens_habit_and_lists_three_points():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("проверяет седло в полдень", 0.0)
    text = dragon.check_saddle()
    after = dragon.soul.habits["проверяет седло в полдень"]
    assert after > before
    assert "1." in text and "2." in text and "3." in text
    assert "ремни" in text
    assert "Можно взлетать" in text


def test_check_saddle_remembers_the_ritual():
    dragon = Character(name="Грок")
    dragon.check_saddle()
    recalled = dragon.memory.recall("проверка седла", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "седл" in blob


def test_talk_about_saddle_check_returns_checklist():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("проверяет седло в полдень", 0.0)
    reply = dragon.talk("Проверь седло, три точки")
    after = dragon.soul.habits["проверяет седло в полдень"]
    assert after > before
    assert "крыло" in reply.lower()
