"""Тесты ритуала level_glide."""

from dragonforge import Character


def test_level_glide_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("выравнивает планирование после термика", 0.0)
    text = dragon.level_glide("ровный край над лугом")
    after = dragon.soul.habits["выравнивает планирование после термика"]
    assert after > before
    assert "ровный край над лугом" in text
    assert "планир" in text.lower()


def test_level_glide_default_path():
    dragon = Character(name="Грок")
    text = dragon.level_glide("  ")
    assert "ровный край над лугом" in text


def test_level_glide_is_remembered():
    dragon = Character(name="Грок")
    dragon.level_glide("ровный гребень над тёплым склоном")
    recalled = dragon.memory.recall("планирование", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "планир" in blob or "гребен" in blob or "гребень" in blob


def test_talk_about_glide_levels():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("выравнивает планирование после термика", 0.0)
    reply = dragon.talk("Выровняй планирование над гребнем")
    after = dragon.soul.habits["выравнивает планирование после термика"]
    assert after > before
    assert "планир" in reply.lower() or "гребень" in reply.lower()
    assert "греб" in reply.lower()
