"""В воскресенье 11 октября к вечеру после тихого мурлыканья в седле: тихо дремлет в седле под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_doze_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, спокойный, тихо дремлет в седле",
        backstory="Воскресенье 11 октября, после тихого мурлыканья в седле под тенью, время тихо подремать",
    )
    print(dragon.purr_saddle("тихое мурлыканье в седле под тенью к вечеру"))
    print()
    print(dragon.doze_saddle("тихое дремание в седле под тенью к вечеру"))
    print()
    print(dragon.talk("Дремли в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
