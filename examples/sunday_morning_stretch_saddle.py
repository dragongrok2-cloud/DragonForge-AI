"""В воскресенье 11 октября утром: мягко потягивается в седле под утренним солнцем, крылья раскрывает чуть шире, седло не снимаем.

Запуск: python examples/sunday_morning_stretch_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="утренний, тёплый, потягивается в седле",
        backstory="Воскресенье 11 октября, после ночной дремоты, утро ждёт мягкого потягивания под солнцем",
    )
    print(dragon.drowse_saddle("седло к ночи после уюта"))
    print()
    print(dragon.stretch_saddle("седло под утренним солнцем"))
    print()
    print(dragon.talk("Потянись в седле под солнцем"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
