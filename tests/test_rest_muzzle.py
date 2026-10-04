"""Тесты ритуала rest_muzzle."""

from dragonforge import Character


def test_rest_muzzle_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("кладет морду на луку после хвоста", 0.0)
    text = dragon.rest_muzzle("морда на луке")
    after = dragon.soul.habits["кладет морду на луку после хвоста"]
    assert after > before
    assert "морда на луке" in text
    assert "луку" in text.lower() or "луке" in text.lower()


def test_rest_muzzle_default_spot():
    dragon = Character(name="Грок")
    text = dragon.rest_muzzle("  ")
    assert "морда на луке" in text


def test_rest_muzzle_is_remembered():
    dragon = Character(name="Грок")
    dragon.rest_muzzle("морда у стремени")
    recalled = dragon.memory.recall("морду", n_results=3)
    blob = " ".join(str(item) for item in recalled).lower()
    assert "морду" in blob or "стремен" in blob


def test_talk_about_muzzle_rests():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("кладет морду на луку после хвоста", 0.0)
    reply = dragon.talk("Положи морду у стремени")
    after = dragon.soul.habits["кладет морду на луку после хвоста"]
    assert after > before
    assert "морда" in reply.lower()
    assert "стремен" in reply.lower()
