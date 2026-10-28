"""В воскресенье 11 октября к вечеру после тихого бормотания в седле: тихо зевает в седле под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_yawn_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, спокойный, тихо зевает в седле",
        backstory="Воскресенье 11 октября, после тихого бормотания в седле под тенью, время тихо позевать",
    )
    print(dragon.murmur_saddle("тихое бормотание в седле под тенью к вечеру"))
    print()
    print(dragon.yawn_saddle("тихое зевание в седле под тенью к вечеру"))
    print()
    print(dragon.talk("Зевай в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
