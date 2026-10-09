"""Крошка с полоски солнца после полудня 9 октября."""

from dragonforge import Character


def test_sweep_crumb_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("смахивает крошку с полоски солнца после полудня", 0.0)
    reply = dragon.sweep_crumb("крошка с полоски солнца после полудня")
    after = dragon.soul.habits["смахивает крошку с полоски солнца после полудня"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_sweep_crumb_keeps_share_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("делится яблочной крошкой на полоске солнца в полдень", 0.4)
    dragon.sweep_crumb()
    assert dragon.soul.habits["делится яблочной крошкой на полоске солнца в полдень"] > 0.4


def test_sweep_crumb_is_remembered():
    dragon = Character(name="Грок")
    dragon.sweep_crumb("крошка с полоски солнца над рекой после полудня")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "крош" in blob
    assert "рек" in blob


def test_talk_about_sweep_crumb():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("смахивает крошку с полоски солнца после полудня", 0.0)
    reply = dragon.talk("Смахни крошку после полудня")
    after = dragon.soul.habits["смахивает крошку с полоски солнца после полудня"]
    assert after > before
    assert "седл" in reply.lower()
    assert "делится яблочной крошкой" not in reply.lower()


def test_share_crumb_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Поделись крошкой в полдень")
    assert "крош" in reply.lower() or "полоск" in reply.lower()
    assert "смахивает крошку" not in reply.lower()


def test_tilt_glass_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Наклони стекло к одиннадцати")
    assert "стекл" in reply.lower() or "полоск" in reply.lower()
    assert "смахивает крошку" not in reply.lower()
