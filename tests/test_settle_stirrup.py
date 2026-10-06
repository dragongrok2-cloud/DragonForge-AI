"""Тесты ритуала settle_stirrup."""

from dragonforge import Character


def test_settle_stirrup_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("выравнивает стремя после опущенного края", 0.0)
    text = dragon.settle_stirrup("стремя после опущенного края")
    after = dragon.soul.habits["выравнивает стремя после опущенного края"]
    assert after > before
    assert "стремя после опущенного края" in text
    assert "стрем" in text.lower()
    assert "седл" in text.lower()


def test_settle_stirrup_default_place():
    dragon = Character(name="Грок")
    text = dragon.settle_stirrup("  ")
    assert "стремя после опущенного края" in text


def test_settle_stirrup_is_remembered():
    dragon = Character(name="Грок")
    dragon.settle_stirrup("стремя над рекой после опущенного края")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "стрем" in blob
    assert "рек" in blob


def test_talk_about_settle_stirrup():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("выравнивает стремя после опущенного края", 0.0)
    reply = dragon.talk("Выровняй стремя после края крыла")
    after = dragon.soul.habits["выравнивает стремя после опущенного края"]
    assert after > before
    assert "стрем" in reply.lower()
    assert "седл" in reply.lower()


def test_ease_wing_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Опусти край крыла после тени")
    assert "крыл" in reply.lower()
    assert "выравнивает стремя" not in reply.lower()