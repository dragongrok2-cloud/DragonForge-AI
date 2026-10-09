"""После полудня 9 октября: полоска солнца на костяшках, седло не снимаем.

Запуск: python examples/friday_afternoon_shift_stripe.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, греет костяшки полоской",
        backstory="После полудня 9 октября ладонь уже лежала на светлой полоске на Мёде, Шве и Седле",
    )
    print(dragon.rest_stripe("ладонь на светлой полоске после полудня"))
    print()
    print(dragon.shift_stripe("полоска солнца на костяшках после полудня"))
    print()
    print(dragon.talk("Сдвинь полоску на костяшки над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
