"""В воскресенье 11 октября к вечеру после тихого прижатия челюстью: тихо прижимается шеей к седлу под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_rest_neck_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, тёплый, тихо прижимается шеей",
        backstory="Воскресенье 11 октября, после тихого прижатия челюстью под тенью, время тихо прижаться шеей",
    )
    print(dragon.rest_jaw_saddle("тихое прижатие челюсти к седлу под тенью к вечеру"))
    print()
    print(dragon.rest_neck_saddle("тихое прижатие шеи к седлу под тенью к вечеру"))
    print()
    print(dragon.talk("Прижмись шеей к седлу"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
