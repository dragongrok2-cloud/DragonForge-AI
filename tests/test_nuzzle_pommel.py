"""Прижать морду к луке утром 10 октября после тёплого выдоха."""

from dragonforge import Character


def test_nuzzle_pommel_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("прижимает морду к луке после тёплого выдоха", 0.0)
    reply = dragon.nuzzle_pommel("луку утром после выдоха")
    after = dragon.soul.habits["прижимает морду к луке после тёплого выдоха"]
    assert after > before
    assert "лук" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()
    assert "морд" in reply.lower() or "прижим" in reply.lower()


def test_nuzzle_pommel_keeps_huff_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("дышит теплом на луку после обвода", 0.4)
    dragon.nuzzle_pommel()
    assert dragon.soul.habits.get("дышит теплом на луку после обвода", 0.0) >= 0.4


def test_nuzzle_pommel_is_remembered():
    dragon = Character(name="Грок")
    dragon.nuzzle_pommel("луку над рекой утром после выдоха")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "лук" in blob or "морд" in blob
    assert "рек" in blob


def test_talk_about_nuzzle_pommel():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("прижимает морду к луке после тёплого выдоха", 0.0)
    reply = dragon.talk("Прижми морду к луке")
    after = dragon.soul.habits["прижимает морду к луке после тёплого выдоха"]
    assert after > before
    assert "седл" in reply.lower()
