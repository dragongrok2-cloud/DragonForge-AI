"""Тесты субботней подпруги после росы."""

from dragonforge import Character


def test_cinch_girth_strengthens_habit_and_trust():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("подтягивает подпругу после росы", 0.0)
    trust_before = dragon.soul.emotional_state.get("trust", 0.5)
    text = dragon.cinch_girth("на одну дырочку")
    after = dragon.soul.habits["подтягивает подпругу после росы"]
    assert after > before
    assert dragon.soul.emotional_state["trust"] > trust_before
    assert "дырочку" in text
    assert "подпруг" in text.lower()


def test_cinch_girth_is_remembered():
    dragon = Character(name="Грок")
    dragon.cinch_girth("на две дырочки")
    recalled = dragon.memory.recall("подпругу", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "подпруг" in blob or "седл" in blob


def test_talk_about_girth_cinches():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("подтягивает подпругу после росы", 0.0)
    reply = dragon.talk("Подтяни подпругу на две дырочки")
    after = dragon.soul.habits["подтягивает подпругу после росы"]
    assert after > before
    assert "подпруг" in reply.lower()
    assert "две" in reply.lower()
