"""Тесты послеполуденной тени крыла."""

from dragonforge import Character


def test_offer_shade_strengthens_habit_and_energy():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("даёт тень крылом после полудня", 0.0)
    energy_before = dragon.soul.emotional_state.get("energy", 0.5)
    text = dragon.offer_shade()
    after = dragon.soul.habits["даёт тень крылом после полудня"]
    assert after > before
    assert dragon.soul.emotional_state["energy"] > energy_before
    assert "тень" in text.lower()
    assert "Можно лететь дальше" in text


def test_offer_shade_remembers_the_ritual():
    dragon = Character(name="Грок")
    dragon.offer_shade()
    recalled = dragon.memory.recall("тень крылом", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "тень" in blob


def test_talk_about_shade_returns_canopy():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("даёт тень крылом после полудня", 0.0)
    reply = dragon.talk("Дай тень крыла после полудня")
    after = dragon.soul.habits["даёт тень крылом после полудня"]
    assert after > before
    assert "седл" in reply.lower()
