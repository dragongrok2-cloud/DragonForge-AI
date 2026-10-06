"""Тесты ритуала tuck_strap."""

from dragonforge import Character


def test_tuck_strap_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("подворачивает конец ремня после тихой пряжки", 0.0)
    text = dragon.tuck_strap("конец ремня после тихой пряжки")
    after = dragon.soul.habits["подворачивает конец ремня после тихой пряжки"]
    assert after > before
    assert "конец ремня после тихой пряжки" in text
    assert "ремн" in text.lower()
    assert "седл" in text.lower()


def test_tuck_strap_default_place():
    dragon = Character(name="Грок")
    text = dragon.tuck_strap("  ")
    assert "конец ремня после тихой пряжки" in text


def test_tuck_strap_is_remembered():
    dragon = Character(name="Грок")
    dragon.tuck_strap("конец ремня над рекой после тихой пряжки")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "ремн" in blob
    assert "рек" in blob


def test_talk_about_tuck_strap():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("подворачивает конец ремня после тихой пряжки", 0.0)
    reply = dragon.talk("Подогни конец ремня, чтобы не хлопал")
    after = dragon.soul.habits["подворачивает конец ремня после тихой пряжки"]
    assert after > before
    assert "ремн" in reply.lower()
    assert "седл" in reply.lower()


def test_snug_buckle_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Прижми пряжку после стремени")
    assert "пряж" in reply.lower()
    assert "подворачивает конец ремня" not in reply.lower()
