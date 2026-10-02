"""Тесты мягкой посадки перед выходными."""

from dragonforge import Character


def test_soft_landing_strengthens_habit():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("мягко садится перед выходными", 0.0)
    text = dragon.soft_landing()
    after = dragon.soul.habits["мягко садится перед выходными"]
    assert after > before
    assert "посадк" in text.lower() or "Посадка" in text
    assert "седло" in text.lower()


def test_low_energy_landing_mentions_rest():
    dragon = Character(name="Грок")
    dragon.soul.emotional_state["energy"] = 0.3
    text = dragon.soft_landing()
    assert "Энергии мало" in text
    assert "0.30" in text


def test_talk_about_weekend_evolves_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("мягко садится перед выходными", 0.0)
    reply = dragon.talk("Пора садиться, выходные близко")
    after = dragon.soul.habits["мягко садится перед выходными"]
    assert after > before
    assert "крыло" in reply.lower()
