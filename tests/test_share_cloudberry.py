"""Тесты послеполуденной облачной ягоды."""

from dragonforge import Character


def test_share_cloudberry_strengthens_habit_and_joy():
    dragon = Character(name="Грок", species="Добрый дракон с седлом")
    before = dragon.soul.habits.get("делится облачной ягодой после поводьев", 0.0)
    joy_before = dragon.soul.emotional_state.get("joy", 0.5)
    text = dragon.share_cloudberry("морошка")
    after = dragon.soul.habits["делится облачной ягодой после поводьев"]
    assert after > before
    assert dragon.soul.emotional_state["joy"] > joy_before
    assert "ягод" in text.lower()
    assert "морошка" in text


def test_share_cloudberry_is_remembered():
    dragon = Character(name="Грок")
    dragon.share_cloudberry("облачная ягода")
    recalled = dragon.memory.recall("ягода", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "ягод" in blob or "седл" in blob


def test_talk_about_berry_shares():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("делится облачной ягодой после поводьев", 0.0)
    reply = dragon.talk("Поделись ягодой, морошка из седельной сумки")
    after = dragon.soul.habits["делится облачной ягодой после поводьев"]
    assert after > before
    assert "ягод" in reply.lower()
    assert "морошка" in reply.lower()
