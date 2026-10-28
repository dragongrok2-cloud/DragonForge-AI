"""В воскресенье 11 октября к вечеру после тихого дремания в седле: тихо прижимается мордой к седлу под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_nuzzle_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, тёплый, тихо прижимается к седлу",
        backstory="Воскресенье 11 октября, после тихого дремания в седле под тенью, время тихо прижаться мордой",
    )
    print(dragon.doze_saddle("тихое дремание в седле под тенью к вечеру"))
    print()
    print(dragon.nuzzle_saddle("тихое прижатие морды к седлу под тенью к вечеру"))
    print()
    print(dragon.talk("Прижмись к седлу"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
