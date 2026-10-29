"""Тест ритуала rest_wingtip_saddle."""

from dragonforge import Character


def test_rest_wingtip_saddle_strengthens_habit():
    dragon = Character(name="Тест")
    before = dragon.soul.habits.get("тихо кладёт кончик крыла на седло под тенью к вечеру", 0.0)
    result = dragon.rest_wingtip_saddle("тест")
    after = dragon.soul.habits.get("тихо кладёт кончик крыла на седло под тенью к вечеру", 0.0)
    assert after > before
    assert "кончик" in result.lower() or "крыла" in result.lower()
    assert "седло" in result.lower()


def test_talk_triggers_wingtip():
    dragon = Character(name="Тест")
    result = dragon.talk("положи кончик крыла на седло")
    assert "кончик" in result.lower() or "крыла" in result.lower()
