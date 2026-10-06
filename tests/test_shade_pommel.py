"""Тесты ритуала shade_pommel."""

from dragonforge import Character


def test_shade_pommel_strengthens_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("держит тень над лукой в полдень", 0.0)
    text = dragon.shade_pommel("тень крыла над лукой в полдень")
    after = dragon.soul.habits["держит тень над лукой в полдень"]
    assert after > before
    assert "тень крыла над лукой в полдень" in text
    assert "лук" in text.lower()
    assert "седл" in text.lower()


def test_shade_pommel_default_place():
    dragon = Character(name="Грок")
    text = dragon.shade_pommel("  ")
    assert "тень крыла над лукой в полдень" in text


def test_shade_pommel_is_remembered():
    dragon = Character(name="Грок")
    dragon.shade_pommel("тень крыла над стременем в полдень")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "тень" in blob
    assert "стрем" in blob or "лук" in blob


def test_talk_about_shade_pommel():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("держит тень над лукой в полдень", 0.0)
    reply = dragon.talk("Придержи крыло тенью над лукой")
    after = dragon.soul.habits["держит тень над лукой в полдень"]
    assert after > before
    assert "лук" in reply.lower()
    assert "седл" in reply.lower()


def test_fold_cloth_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Сложи край попоны после росы")
    assert "попон" in reply.lower()
    assert "тень крыла над лукой" not in reply.lower()
