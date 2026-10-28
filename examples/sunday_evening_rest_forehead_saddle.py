"""В воскресенье 11 октября к вечеру после тихого прижатия щекой: тихо прижимается лбом к седлу под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_rest_forehead_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, тёплый, тихо прижимается лбом",
        backstory="Воскресенье 11 октября, после тихого прижатия щекой под тенью, время тихо прижаться лбом",
    )
    print(dragon.rest_cheek_saddle("тихое прижатие щеки к седлу под тенью к вечеру"))
    print()
    print(dragon.rest_forehead_saddle("тихое прижатие лба к седлу под тенью к вечеру"))
    print()
    print(dragon.talk("Прижмись лбом к седлу"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
