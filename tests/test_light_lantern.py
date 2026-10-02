"""Тесты вечернего фонарика на седле."""

from dragonforge import Character


def test_light_lantern_strengthens_habit_and_joy():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("зажигает фонарик на седле к вечеру", 0.0)
    joy_before = dragon.soul.emotional_state.get("joy", 0.5)
    text = dragon.light_lantern("янтарный")
    after = dragon.soul.habits["зажигает фонарик на седле к вечеру"]
    assert after > before
    assert dragon.soul.emotional_state["joy"] > joy_before
    assert "фонарик" in text.lower() or "огон" in text.lower()
    assert "Можно лететь в сумерки" in text


def test_light_lantern_blue_flame_is_remembered():
    dragon = Character(name="Грок")
    dragon.light_lantern("синий")
    recalled = dragon.memory.recall("фонарик", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "синий" in blob or "фонарик" in blob


def test_talk_about_lantern_lights_it():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("зажигает фонарик на седле к вечеру", 0.0)
    reply = dragon.talk("Зажги фонарик на седле, золотой, к сумеркам")
    after = dragon.soul.habits["зажигает фонарик на седле к вечеру"]
    assert after > before
    assert "седл" in reply.lower()
    assert "золот" in reply.lower()
