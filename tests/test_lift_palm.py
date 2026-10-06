"""Тесты ритуала lift_palm."""

from dragonforge import Character


def test_lift_palm_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("поднимает ладонь после нажатия", 0.0)
    text = dragon.lift_palm("ладонь после ночного нажатия")
    after = dragon.soul.habits["поднимает ладонь после нажатия"]
    assert after > before
    assert "ладонь после ночного нажатия" in text
    assert "ладон" in text.lower()
    assert "седл" in text.lower()


def test_lift_palm_default_place():
    dragon = Character(name="Грок")
    text = dragon.lift_palm("  ")
    assert "ладонь после ночного нажатия" in text


def test_lift_palm_is_remembered():
    dragon = Character(name="Грок")
    dragon.lift_palm("ладонь у луки")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "ладон" in blob
    assert "нажат" in blob or "лук" in blob


def test_talk_about_lift_palm():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("поднимает ладонь после нажатия", 0.0)
    reply = dragon.talk("Подними ладонь утром")
    after = dragon.soul.habits["поднимает ладонь после нажатия"]
    assert after > before
    assert "ладон" in reply.lower()
    assert "седл" in reply.lower()
