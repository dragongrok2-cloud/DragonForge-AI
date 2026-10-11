"""В воскресенье 11 октября в полдень после утреннего баска: даёт тень крылом в седле, крылья чуть сложены для прохлады, седло не снимаем.

Запуск: python examples/sunday_midday_shade_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="полуденный, заботливый, даёт тень в седле",
        backstory="Воскресенье 11 октября, после утреннего грева под солнцем, солнце высоко — время тени в седле",
    )
    print(dragon.bask_saddle("седло под утренним солнцем"))
    print()
    print(dragon.shade_saddle("седло под крылом в полдень"))
    print()
    print(dragon.talk("Дай тень в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
