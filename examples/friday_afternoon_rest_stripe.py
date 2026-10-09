"""После полудня 9 октября: ладонь на светлой полоске, седло не снимаем.

Запуск: python examples/friday_afternoon_rest_stripe.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, греет пальцы о полоску",
        backstory="После полудня 9 октября крошка уже сметена с полоски солнца на Мёде, Шве и Седле",
    )
    print(dragon.sweep_crumb("крошка с полоски солнца после полудня"))
    print()
    print(dragon.rest_stripe("ладонь на светлой полоске после полудня"))
    print()
    print(dragon.talk("Придержи ладонь на полоске над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
