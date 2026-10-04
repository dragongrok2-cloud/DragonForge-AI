"""Тесты ритуала huff_warm."""

from dragonforge import Character


def test_huff_warm_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("дышит теплом после медленного моргания", 0.0)
    text = dragon.huff_warm("тёплый выдох на перчатки")
    after = dragon.soul.habits["дышит теплом после медленного моргания"]
    assert after > before
    assert "тёплый выдох на перчатки" in text
    assert "тепл" in text.lower() or "тёпл" in text.lower()


def test_huff_warm_default_breath():
    dragon = Character(name="Грок")
    text = dragon.huff_warm("  ")
    assert "тёплый выдох на перчатки" in text


def test_huff_warm_is_remembered():
    dragon = Character(name="Грок")
    dragon.huff_warm("тёплый выдох на ладони")
    recalled = dragon.memory.recall("дыхнул", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "дых" in blob or "ладон" in blob


def test_talk_about_warm_huff():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("дышит теплом после медленного моргания", 0.0)
    reply = dragon.talk("Подыши теплом на поводья")
    after = dragon.soul.habits["дышит теплом после медленного моргания"]
    assert after > before
    assert "повод" in reply.lower()
    assert "выдох" in reply.lower()
