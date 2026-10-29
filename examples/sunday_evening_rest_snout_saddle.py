"""В воскресенье 11 октября к вечеру после тихого прижатия лбом: тихо прижимается носом к седлу под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_rest_snout_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, тёплый, тихо прижимается носом",
        backstory="Воскресенье 11 октября, после тихого прижатия лбом под тенью, время тихо прижаться носом",
    )
    print(dragon.rest_forehead_saddle("тихое прижатие лба к седлу под тенью к вечеру"))
    print()
    print(dragon.rest_snout_saddle("тихое прижатие носа к седлу под тенью к вечеру"))
    print()
    print(dragon.talk("Прижмись носом к седлу"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
