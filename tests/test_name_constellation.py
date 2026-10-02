"""Тесты вечернего шёпота созвездий."""

from dragonforge import Character


def test_name_constellation_strengthens_habit_and_curiosity():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("шепчет имена созвездий", 0.0)
    curiosity_before = dragon.soul.emotional_state.get("curiosity", 0.5)
    text = dragon.name_constellation("лебедь")
    after = dragon.soul.habits["шепчет имена созвездий"]
    assert after > before
    assert dragon.soul.emotional_state["curiosity"] > curiosity_before
    assert "Лебедь" in text
    assert "Карта неба с нами" in text


def test_name_constellation_draco_is_remembered():
    dragon = Character(name="Грок")
    dragon.name_constellation("дракон")
    recalled = dragon.memory.recall("созвездие", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "дракон" in blob or "созвезди" in blob


def test_talk_about_stars_names_constellation():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("шепчет имена созвездий", 0.0)
    reply = dragon.talk("Шепни звёзды: назови созвездие Кассиопея")
    after = dragon.soul.habits["шепчет имена созвездий"]
    assert after > before
    assert "кассиопея" in reply.lower()
    assert "седл" in reply.lower()
