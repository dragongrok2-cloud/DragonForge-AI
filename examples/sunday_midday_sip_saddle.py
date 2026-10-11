"""В воскресенье 11 октября в полдень после тени крыла: делает глоток в седле, термос или облачная ягода, седло не снимаем.

Запуск: python examples/sunday_midday_sip_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="полуденный, заботливый, делится глотком в седле",
        backstory="Воскресенье 11 октября, после тени крыла в полдень, время глотка в прохладе седла",
    )
    print(dragon.shade_saddle("седло под крылом в полдень"))
    print()
    print(dragon.sip_saddle("глоток в седле под тенью в полдень"))
    print()
    print(dragon.talk("Сделай глоток в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
