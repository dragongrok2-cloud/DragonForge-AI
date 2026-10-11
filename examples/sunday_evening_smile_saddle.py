"""В воскресенье 11 октября к вечеру после тихого закрытия глаз в седле: тихо улыбается в седле под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_smile_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, спокойный, улыбается в седле",
        backstory="Воскресенье 11 октября, после тихого закрытия глаз в седле под тенью, время тихо улыбнуться",
    )
    print(dragon.close_eyes_saddle("тихое закрытие глаз в седле под тенью после полудня"))
    print()
    print(dragon.smile_saddle("тихая улыбка в седле под тенью к вечеру"))
    print()
    print(dragon.talk("Улыбнись в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
