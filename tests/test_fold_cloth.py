"""Тесты ритуала fold_cloth."""

from dragonforge import Character


def test_fold_cloth_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("складывает край попоны после росы", 0.0)
    text = dragon.fold_cloth("край попоны под лукой после росы")
    after = dragon.soul.habits["складывает край попоны после росы"]
    assert after > before
    assert "край попоны под лукой после росы" in text
    assert "попон" in text.lower()
    assert "седл" in text.lower()


def test_fold_cloth_default_place():
    dragon = Character(name="Грок")
    text = dragon.fold_cloth("  ")
    assert "край попоны под лукой после росы" in text


def test_fold_cloth_is_remembered():
    dragon = Character(name="Грок")
    dragon.fold_cloth("край попоны у седельной сумки")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "попон" in blob
    assert "лук" in blob or "сумк" in blob


def test_talk_about_fold_cloth():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("складывает край попоны после росы", 0.0)
    reply = dragon.talk("Сложи край попоны после росы")
    after = dragon.soul.habits["складывает край попоны после росы"]
    assert after > before
    assert "попон" in reply.lower()
    assert "седл" in reply.lower()


def test_blot_scale_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Промокни чешуйку после ладони")
    assert "чешу" in reply.lower()
    assert "попону под луку" not in reply.lower()
