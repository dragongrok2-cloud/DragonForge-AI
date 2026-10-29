"""В воскресенье 11 октября к вечеру после тихого прижатия носом: тихо прижимается ухом к седлу под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_rest_ear_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, тёплый, тихо прижимается ухом",
        backstory="Воскресенье 11 октября, после тихого прижатия носом под тенью, время тихо прижаться ухом",
    )
    print(dragon.rest_snout_saddle("тихое прижатие носа к седлу под тенью к вечеру"))
    print()
    print(dragon.rest_ear_saddle("тихое прижатие уха к седлу под тенью к вечеру"))
    print()
    print(dragon.talk("Прижмись ухом к седлу"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
