"""Полоска солнца на сухом стекле фонарика к одиннадцати 9 октября."""

from dragonforge import Character


def test_tilt_glass_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("наклоняет сухое стекло фонарика к одиннадцати", 0.0)
    reply = dragon.tilt_glass("полоска солнца на сухом стекле к одиннадцати")
    after = dragon.soul.habits["наклоняет сухое стекло фонарика к одиннадцати"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_tilt_glass_keeps_bead_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("промокает бусинку росы со стекла фонарика к середине утра", 0.4)
    dragon.tilt_glass()
    assert dragon.soul.habits["промокает бусинку росы со стекла фонарика к середине утра"] > 0.4


def test_tilt_glass_is_remembered():
    dragon = Character(name="Грок")
    dragon.tilt_glass("полоска солнца на сухом стекле над рекой к одиннадцати")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "стекл" in blob or "полоск" in blob
    assert "рек" in blob


def test_talk_about_tilt_glass():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("наклоняет сухое стекло фонарика к одиннадцати", 0.0)
    reply = dragon.talk("Наклони стекло к одиннадцати")
    after = dragon.soul.habits["наклоняет сухое стекло фонарика к одиннадцати"]
    assert after > before
    assert "седл" in reply.lower()
    assert "промокает бусинку" not in reply.lower()


def test_blot_bead_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Промокни бусинку росы со стекла")
    assert "бусин" in reply.lower() or "рос" in reply.lower()
    assert "наклоняет сухое стекло" not in reply.lower()


def test_cup_glow_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Согрей ладони о стекло фонарика")
    assert "ладон" in reply.lower() or "стекл" in reply.lower()
    assert "наклоняет сухое стекло" not in reply.lower()
