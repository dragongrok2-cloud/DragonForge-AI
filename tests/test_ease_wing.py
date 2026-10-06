"""Тесты ритуала ease_wing."""

from dragonforge import Character


def test_ease_wing_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("опускает край крыла после полуденной тени", 0.0)
    text = dragon.ease_wing("край крыла после полуденной тени")
    after = dragon.soul.habits["опускает край крыла после полуденной тени"]
    assert after > before
    assert "край крыла после полуденной тени" in text
    assert "крыл" in text.lower()
    assert "седл" in text.lower()


def test_ease_wing_default_place():
    dragon = Character(name="Грок")
    text = dragon.ease_wing("  ")
    assert "край крыла после полуденной тени" in text


def test_ease_wing_is_remembered():
    dragon = Character(name="Грок")
    dragon.ease_wing("край крыла над рекой после полуденной тени")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "крыл" in blob
    assert "рек" in blob or "тен" in blob


def test_talk_about_ease_wing():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("опускает край крыла после полуденной тени", 0.0)
    reply = dragon.talk("Опусти край крыла после тени")
    after = dragon.soul.habits["опускает край крыла после полуденной тени"]
    assert after > before
    assert "крыл" in reply.lower()
    assert "седл" in reply.lower()


def test_shade_pommel_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Придержи крыло тенью над лукой")
    assert "лук" in reply.lower()
    assert "опускает край" not in reply.lower()
