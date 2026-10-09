"""Яблочная крошка на полоске солнца в полдень 9 октября."""

from dragonforge import Character


def test_share_crumb_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("делится яблочной крошкой на полоске солнца в полдень", 0.0)
    reply = dragon.share_crumb("яблочная крошка на полоске солнца в полдень")
    after = dragon.soul.habits["делится яблочной крошкой на полоске солнца в полдень"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_share_crumb_keeps_tilt_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("наклоняет сухое стекло фонарика к одиннадцати", 0.4)
    dragon.share_crumb()
    assert dragon.soul.habits["наклоняет сухое стекло фонарика к одиннадцати"] > 0.4


def test_share_crumb_is_remembered():
    dragon = Character(name="Грок")
    dragon.share_crumb("яблочная крошка на полоске солнца над рекой в полдень")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "крош" in blob
    assert "рек" in blob


def test_talk_about_share_crumb():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("делится яблочной крошкой на полоске солнца в полдень", 0.0)
    reply = dragon.talk("Поделись крошкой в полдень")
    after = dragon.soul.habits["делится яблочной крошкой на полоске солнца в полдень"]
    assert after > before
    assert "седл" in reply.lower()
    assert "наклоняет сухое стекло" not in reply.lower()


def test_tilt_glass_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Наклони стекло к одиннадцати")
    assert "стекл" in reply.lower() or "полоск" in reply.lower()
    assert "делится яблочной крошкой" not in reply.lower()


def test_blot_bead_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Промокни бусинку росы со стекла")
    assert "бусин" in reply.lower() or "рос" in reply.lower()
    assert "делится яблочной крошкой" not in reply.lower()
