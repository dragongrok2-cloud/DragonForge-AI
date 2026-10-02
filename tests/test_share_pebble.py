"""Тесты послеполётного дара камушка."""

from dragonforge import Character


def test_share_pebble_strengthens_habit_and_joy():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("собирает блестящие камушки", 0.0)
    joy_before = dragon.soul.emotional_state["joy"]
    text = dragon.share_pebble(place="седло")
    after = dragon.soul.habits["собирает блестящие камушки"]
    assert after > before
    assert dragon.soul.emotional_state["joy"] > joy_before
    assert "камушек" in text.lower()
    assert "седло" in text.lower()


def test_share_pebble_is_remembered():
    dragon = Character(name="Грок")
    dragon.share_pebble()
    recalled = dragon.memory.recall("подарил камушек", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "камуш" in blob


def test_talk_asks_for_pebble_gift():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("собирает блестящие камушки", 0.0)
    reply = dragon.talk("Подари камушек в седло")
    after = dragon.soul.habits["собирает блестящие камушки"]
    assert after > before
    assert "камуш" in reply.lower()
