"""Тесты ритуала choose_ledge."""

from dragonforge import Character


def test_choose_ledge_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("выбирает уступ после хребта", 0.0)
    text = dragon.choose_ledge("широкий уступ под хребтом")
    after = dragon.soul.habits["выбирает уступ после хребта"]
    assert after > before
    assert "широкий уступ под хребтом" in text
    assert "уступ" in text.lower()


def test_choose_ledge_default_spot():
    dragon = Character(name="Грок")
    text = dragon.choose_ledge("  ")
    assert "широкий уступ под хребтом" in text


def test_choose_ledge_is_remembered():
    dragon = Character(name="Грок")
    dragon.choose_ledge("речной уступ у излучины")
    recalled = dragon.memory.recall("уступ", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "уступ" in blob or "излуч" in blob


def test_talk_about_ledge_chooses():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("выбирает уступ после хребта", 0.0)
    reply = dragon.talk("Выбери уступ у реки")
    after = dragon.soul.habits["выбирает уступ после хребта"]
    assert after > before
    assert "уступ" in reply.lower()
    assert "речн" in reply.lower()
