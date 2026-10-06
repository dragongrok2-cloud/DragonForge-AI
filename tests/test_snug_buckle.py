"""Тесты ритуала snug_buckle."""

from dragonforge import Character


def test_snug_buckle_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("прижимает пряжку после ровного стремени", 0.0)
    text = dragon.snug_buckle("пряжка после ровного стремени")
    after = dragon.soul.habits["прижимает пряжку после ровного стремени"]
    assert after > before
    assert "пряжка после ровного стремени" in text
    assert "пряж" in text.lower()
    assert "седл" in text.lower()


def test_snug_buckle_default_place():
    dragon = Character(name="Грок")
    text = dragon.snug_buckle("  ")
    assert "пряжка после ровного стремени" in text


def test_snug_buckle_is_remembered():
    dragon = Character(name="Грок")
    dragon.snug_buckle("пряжка над рекой после ровного стремени")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "пряж" in blob
    assert "рек" in blob


def test_talk_about_snug_buckle():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("прижимает пряжку после ровного стремени", 0.0)
    reply = dragon.talk("Прижми пряжку после стремени")
    after = dragon.soul.habits["прижимает пряжку после ровного стремени"]
    assert after > before
    assert "пряж" in reply.lower()
    assert "седл" in reply.lower()


def test_settle_stirrup_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Выровняй стремя после края крыла")
    assert "стрем" in reply.lower()
    assert "прижимает пряжку" not in reply.lower()
