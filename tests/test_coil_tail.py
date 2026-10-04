"""Тесты ритуала coil_tail."""

from dragonforge import Character


def test_coil_tail_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("сворачивает хвост после уступа", 0.0)
    text = dragon.coil_tail("кольцо у луки")
    after = dragon.soul.habits["сворачивает хвост после уступа"]
    assert after > before
    assert "кольцо у луки" in text
    assert "хвост" in text.lower()


def test_coil_tail_default_ring():
    dragon = Character(name="Грок")
    text = dragon.coil_tail("  ")
    assert "кольцо у луки" in text


def test_coil_tail_is_remembered():
    dragon = Character(name="Грок")
    dragon.coil_tail("кольцо у стремени")
    recalled = dragon.memory.recall("хвост", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "хвост" in blob or "стремен" in blob


def test_talk_about_tail_coils():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("сворачивает хвост после уступа", 0.0)
    reply = dragon.talk("Сверни хвост у стремени")
    after = dragon.soul.habits["сворачивает хвост после уступа"]
    assert after > before
    assert "хвост" in reply.lower()
    assert "стремен" in reply.lower()
