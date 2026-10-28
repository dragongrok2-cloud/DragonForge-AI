"""В воскресенье 11 октября к вечеру после тихого зевка в седле: тихо мурлычет в седле под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_purr_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, спокойный, тихо мурлычет в седле",
        backstory="Воскресенье 11 октября, после тихого зевка в седле под тенью, время тихо помурлыкать",
    )
    print(dragon.yawn_saddle("тихое зевание в седле под тенью к вечеру"))
    print()
    print(dragon.purr_saddle("тихое мурлыканье в седле под тенью к вечеру"))
    print()
    print(dragon.talk("Мурлычи в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
