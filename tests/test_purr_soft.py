"""Тесты ритуала purr_soft."""

from dragonforge import Character


def test_purr_soft_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("мурлычет в седло после щеки у колена", 0.0)
    text = dragon.purr_soft("тихое мурлыканье в седло")
    after = dragon.soul.habits["мурлычет в седло после щеки у колена"]
    assert after > before
    assert "тихое мурлыканье в седло" in text
    assert "мурл" in text.lower()


def test_purr_soft_default_rumble():
    dragon = Character(name="Грок")
    text = dragon.purr_soft("  ")
    assert "тихое мурлыканье в седло" in text


def test_purr_soft_is_remembered():
    dragon = Character(name="Грок")
    dragon.purr_soft("мурлыканье у гнезда")
    recalled = dragon.memory.recall("мурлыканье", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "мурл" in blob or "гнезд" in blob


def test_talk_about_purr_soft():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("мурлычет в седло после щеки у колена", 0.0)
    reply = dragon.talk("Помурлычь у колена")
    after = dragon.soul.habits["мурлычет в седло после щеки у колена"]
    assert after > before
    assert "колен" in reply.lower()
    assert "мурл" in reply.lower()
