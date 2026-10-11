"""В воскресенье 11 октября после тихого вздоха в седле: тихо закрывает глаза в седле под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_afternoon_close_eyes_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="полуденный, спокойный, закрывает глаза в седле",
        backstory="Воскресенье 11 октября, после тихого вздоха в седле под тенью, время тихо закрыть глаза",
    )
    print(dragon.sigh_saddle("тихий вздох в седле под тенью после полудня"))
    print()
    print(dragon.close_eyes_saddle("тихое закрытие глаз в седле под тенью после полудня"))
    print()
    print(dragon.talk("Закрой глаза в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
