"""В воскресенье 11 октября к вечеру после тихого прижатия ухом: тихо прижимается челюстью к седлу под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_rest_jaw_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, тёплый, тихо прижимается челюстью",
        backstory="Воскресенье 11 октября, после тихого прижатия ухом под тенью, время тихо прижаться челюстью",
    )
    print(dragon.rest_ear_saddle("тихое прижатие уха к седлу под тенью к вечеру"))
    print()
    print(dragon.rest_jaw_saddle("тихое прижатие челюсти к седлу под тенью к вечеру"))
    print()
    print(dragon.talk("Прижмись челюстью к седлу"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
