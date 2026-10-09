"""Бусинка росы со стекла фонарика к середине утра 9 октября."""

from dragonforge import Character


def test_blot_bead_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("промокает бусинку росы со стекла фонарика к середине утра", 0.0)
    reply = dragon.blot_bead("бусинка росы со стекла фонарика к середине утра")
    after = dragon.soul.habits["промокает бусинку росы со стекла фонарика к середине утра"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_blot_bead_keeps_cup_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("согревает ладони о стекло фонарика под краем утром", 0.4)
    dragon.blot_bead()
    assert dragon.soul.habits["согревает ладони о стекло фонарика под краем утром"] > 0.4


def test_blot_bead_is_remembered():
    dragon = Character(name="Грок")
    dragon.blot_bead("бусинка росы со стекла фонарика над рекой к середине утра")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "бусин" in blob or "рос" in blob
    assert "рек" in blob


def test_talk_about_blot_bead():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("промокает бусинку росы со стекла фонарика к середине утра", 0.0)
    reply = dragon.talk("Промокни бусинку росы со стекла")
    after = dragon.soul.habits["промокает бусинку росы со стекла фонарика к середине утра"]
    assert after > before
    assert "седл" in reply.lower()
    assert "согревает ладони" not in reply.lower()


def test_cup_glow_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Согрей ладони о стекло фонарика")
    assert "ладон" in reply.lower() or "стекл" in reply.lower()
    assert "промокает бусинку" not in reply.lower()


def test_tuck_lantern_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Подсунь фонарик под край попоны")
    assert "фонар" in reply.lower() or "край" in reply.lower()
    assert "промокает бусинку" not in reply.lower()
