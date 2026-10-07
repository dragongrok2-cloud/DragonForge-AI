"""Конец нитки под стежками к полудню после названного цвета."""

from dragonforge import Character


def test_tuck_thread_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("прижимает конец нитки к полудню", 0.0)
    reply = dragon.tuck_thread("конец нитки под стежками к полудню")
    after = dragon.soul.habits["прижимает конец нитки к полудню"]
    assert after > before
    assert "нит" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_tuck_thread_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("называет цвет нитки на стежках к позднему утру", 0.4)
    dragon.tuck_thread()
    assert dragon.soul.habits["называет цвет нитки на стежках к позднему утру"] > 0.4


def test_tuck_thread_is_remembered():
    dragon = Character(name="Грок")
    dragon.tuck_thread("конец нитки под стежками над рекой к полудню")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "нит" in blob
    assert "рек" in blob


def test_talk_about_tuck_thread():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("прижимает конец нитки к полудню", 0.0)
    reply = dragon.talk("Прижми конец нитки под стежки, подворот не трогай")
    after = dragon.soul.habits["прижимает конец нитки к полудню"]
    assert after > before
    assert "нит" in reply.lower()
    assert "седл" in reply.lower()


def test_name_thread_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Назови цвет нитки на стежках, подворот не трогай")
    assert "нит" in reply.lower()
    assert "прижимает конец нитки" not in reply.lower()
