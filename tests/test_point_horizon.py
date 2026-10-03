"""Тесты ритуала point_horizon."""

from dragonforge import Character


def test_point_horizon_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("указывает горизонт после ягоды", 0.0)
    text = dragon.point_horizon("запад")
    after = dragon.soul.habits["указывает горизонт после ягоды"]
    assert after > before
    assert "запад" in text
    assert "горизонт" in text.lower()


def test_point_horizon_default_bearing():
    dragon = Character(name="Грок")
    text = dragon.point_horizon("  ")
    assert "запад" in text


def test_point_horizon_is_remembered():
    dragon = Character(name="Грок")
    dragon.point_horizon("восток")
    recalled = dragon.memory.recall("горизонт", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "горизонт" in blob or "восток" in blob


def test_talk_about_horizon_points():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("указывает горизонт после ягоды", 0.0)
    reply = dragon.talk("Укажи горизонт, куда летим на север")
    after = dragon.soul.habits["указывает горизонт после ягоды"]
    assert after > before
    assert "горизонт" in reply.lower()
    assert "север" in reply.lower()
