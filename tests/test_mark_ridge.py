"""Тесты ритуала mark_ridge."""

from dragonforge import Character


def test_mark_ridge_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("отмечает хребет после планирования", 0.0)
    text = dragon.mark_ridge("дальний хребет над лугом")
    after = dragon.soul.habits["отмечает хребет после планирования"]
    assert after > before
    assert "дальний хребет над лугом" in text
    assert "хреб" in text.lower()


def test_mark_ridge_default_mark():
    dragon = Character(name="Грок")
    text = dragon.mark_ridge("  ")
    assert "дальний хребет над лугом" in text


def test_mark_ridge_is_remembered():
    dragon = Character(name="Грок")
    dragon.mark_ridge("речной хребет у излучины")
    recalled = dragon.memory.recall("хребет", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "хреб" in blob or "излуч" in blob


def test_talk_about_ridge_marks():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("отмечает хребет после планирования", 0.0)
    reply = dragon.talk("Отметь хребет у реки")
    after = dragon.soul.habits["отмечает хребет после планирования"]
    assert after > before
    assert "хреб" in reply.lower()
    assert "речн" in reply.lower()
