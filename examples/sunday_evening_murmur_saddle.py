"""В воскресенье 11 октября к вечеру после тихого опирания подбородком в седле: тихо бормочет в седле под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_murmur_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, спокойный, тихо бормочет в седле",
        backstory="Воскресенье 11 октября, после тихого опирания подбородком в седле под тенью, время тихо бормотать",
    )
    print(dragon.rest_chin_saddle("тихое опирание подбородком в седле под тенью к вечеру"))
    print()
    print(dragon.murmur_saddle("тихое бормотание в седле под тенью к вечеру"))
    print()
    print(dragon.talk("Бормочи в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
