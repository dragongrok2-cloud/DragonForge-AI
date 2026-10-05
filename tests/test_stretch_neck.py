"""Тесты ритуала stretch_neck."""

from dragonforge import Character


def test_stretch_neck_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("тянет шею после тихого мурлыканья", 0.0)
    text = dragon.stretch_neck("тихая потяжка шеи над седлом")
    after = dragon.soul.habits["тянет шею после тихого мурлыканья"]
    assert after > before
    assert "тихая потяжка шеи над седлом" in text
    assert "ше" in text.lower()


def test_stretch_neck_default_reach():
    dragon = Character(name="Грок")
    text = dragon.stretch_neck("  ")
    assert "тихая потяжка шеи над седлом" in text


def test_stretch_neck_is_remembered():
    dragon = Character(name="Грок")
    dragon.stretch_neck("утренняя потяжка шеи")
    recalled = dragon.memory.recall("потяжка", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "ше" in blob or "потяж" in blob


def test_talk_about_stretch_neck():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("тянет шею после тихого мурлыканья", 0.0)
    reply = dragon.talk("Потяни шею над седлом")
    after = dragon.soul.habits["тянет шею после тихого мурлыканья"]
    assert after > before
    assert "седл" in reply.lower()
    assert "ше" in reply.lower()
