"""В воскресенье 11 октября к вечеру после тихого прижатия плечом: тихо прижимается локтем к седлу под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_rest_elbow_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, тёплый, тихо прижимается локтем",
        backstory="Воскресенье 11 октября, после тихого прижатия плечом под тенью, время тихо прижаться локтем",
    )
    print(dragon.rest_shoulder_saddle("тихое прижатие плеча к седлу под тенью к вечеру"))
    print()
    print(dragon.rest_elbow_saddle("тихое прижатие локтя к седлу под тенью к вечеру"))
    print()
    print(dragon.talk("Прижмись локтем к седлу"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
