"""В воскресенье 11 октября к вечеру после тихого прижатия локтем: тихо прижимается запястьем к седлу под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_rest_wrist_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, тёплый, тихо прижимается запястьем",
        backstory="Воскресенье 11 октября, после тихого прижатия локтем под тенью, время тихо прижаться запястьем",
    )
    print(dragon.rest_elbow_saddle("тихое прижатие локтя к седлу под тенью к вечеру"))
    print()
    print(dragon.rest_wrist_saddle("тихое прижатие запястья к седлу под тенью к вечеру"))
    print()
    print(dragon.talk("Прижмись запястьем к седлу"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
