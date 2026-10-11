"""В воскресенье 11 октября утром после потягивания: посидеть и погреться в седле под солнцем, крылья чуть раскрыты, седло не снимаем.

Запуск: python examples/sunday_morning_bask_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="утренний, тёплый, греется в седле",
        backstory="Воскресенье 11 октября, после мягкого потягивания, солнце зовёт посидеть в седле",
    )
    print(dragon.stretch_saddle("седло под утренним солнцем"))
    print()
    print(dragon.bask_saddle("седло под утренним солнцем"))
    print()
    print(dragon.talk("Погрейся в седле под солнцем"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
