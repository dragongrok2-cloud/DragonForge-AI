"""Тесты ритуала shake_leaves."""

from dragonforge import Character


def test_shake_leaves_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("стряхивает кленовые листья после потяжки шеи", 0.0)
    text = dragon.shake_leaves("кленовый лист с луки")
    after = dragon.soul.habits["стряхивает кленовые листья после потяжки шеи"]
    assert after > before
    assert "кленовый лист с луки" in text
    assert "лист" in text.lower()


def test_shake_leaves_default_leaf():
    dragon = Character(name="Грок")
    text = dragon.shake_leaves("  ")
    assert "кленовый лист с луки" in text


def test_shake_leaves_is_remembered():
    dragon = Character(name="Грок")
    dragon.shake_leaves("кленовый лист со стремени")
    recalled = dragon.memory.recall("кленовый", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "кленов" in blob or "лист" in blob


def test_talk_about_shake_leaves():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("стряхивает кленовые листья после потяжки шеи", 0.0)
    reply = dragon.talk("Стряхни кленовые листья с седла")
    after = dragon.soul.habits["стряхивает кленовые листья после потяжки шеи"]
    assert after > before
    assert "седл" in reply.lower()
    assert "лист" in reply.lower()
