"""Цвет нитки на стежках к позднему утру после счёта."""

from dragonforge import Character


def test_name_thread_grows_habit():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("называет цвет нитки на стежках к позднему утру", 0.0)
    reply = dragon.name_thread("цвет нитки на стежках к позднему утру")
    after = dragon.soul.habits["называет цвет нитки на стежках к позднему утру"]
    assert after > before
    assert "нит" in reply.lower()
    assert "седл" in reply.lower()
    assert "не снимаем" in reply.lower()


def test_name_thread_keeps_previous_habit():
    dragon = Character(name="Грок")
    dragon.soul.add_habit("считает стежки на тёплой складке утром", 0.4)
    dragon.name_thread()
    assert dragon.soul.habits["считает стежки на тёплой складке утром"] > 0.4


def test_name_thread_is_remembered():
    dragon = Character(name="Грок")
    dragon.name_thread("цвет нитки на стежках над рекой к позднему утру")
    blob = " ".join(dragon.memory.short_term).lower()
    assert "нит" in blob
    assert "рек" in blob


def test_talk_about_name_thread():
    dragon = Character(name="Грок")
    before = dragon.soul.habits.get("называет цвет нитки на стежках к позднему утру", 0.0)
    reply = dragon.talk("Назови цвет нитки на стежках, подворот не трогай")
    after = dragon.soul.habits["называет цвет нитки на стежках к позднему утру"]
    assert after > before
    assert "нит" in reply.lower()
    assert "седл" in reply.lower()


def test_count_stitch_still_answers():
    dragon = Character(name="Грок")
    reply = dragon.talk("Посчитай стежки на складке, подворот не трогай")
    assert "стеж" in reply.lower()
    assert "называет цвет нитки" not in reply.lower()
