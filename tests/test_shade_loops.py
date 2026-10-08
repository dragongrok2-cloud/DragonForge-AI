"""Тень крыла на петлях медового узелка после полудня, после имён."""

from dragonforge import Character


def test_shade_loops_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("накрывает петли медового узелка тенью после полудня", 0.0)
    reply = dragon.shade_loops("тень крыла на петлях медового узелка после полудня")
    after = dragon.soul.habits["накрывает петли медового узелка тенью после полудня"]
    assert after > before
    assert "мёд" in reply.lower() or "шов" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_shade_loops_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("называет петли медового узелка к раннему дню", 0.4)
    dragon.shade_loops()
    assert dragon.soul.habits["называет петли медового узелка к раннему дню"] > 0.4


def test_shade_loops_is_remembered():
    dragon = Character(name="Грок")
    dragon.shade_loops("тень крыла на петлях медового узелка над рекой после полудня")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "петл" in blob or "узел" in blob
    assert "рек" in blob


def test_talk_about_shade_loops():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("накрывает петли медового узелка тенью после полудня", 0.0)
    reply = dragon.talk("Затени петли узелка")
    after = dragon.soul.habits["накрывает петли медового узелка тенью после полудня"]
    assert after > before
    assert "седл" in reply.lower()
    assert "называет петли медового узелка" not in reply.lower()


def test_name_loops_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Назови петли узелка")
    assert "петл" in reply.lower() or "узел" in reply.lower()
    assert "накрывает петли медового узелка" not in reply.lower()
