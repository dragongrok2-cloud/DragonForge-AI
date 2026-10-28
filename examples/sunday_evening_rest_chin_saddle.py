"""В воскресенье 11 октября к вечеру после тихой улыбки в седле: тихо опирается подбородком в седле под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_rest_chin_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, спокойный, опирается подбородком в седле",
        backstory="Воскресенье 11 октября, после тихой улыбки в седле под тенью, время тихо опереться подбородком",
    )
    print(dragon.smile_saddle("тихая улыбка в седле под тенью к вечеру"))
    print()
    print(dragon.rest_chin_saddle("тихое опирание подбородком в седле под тенью к вечеру"))
    print()
    print(dragon.talk("Опрись подбородком в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
