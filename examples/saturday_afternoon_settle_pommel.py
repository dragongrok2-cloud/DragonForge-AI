"""В субботу 10 октября после полудня: после поглаживания тихо опирается ладонью на луку, седло не снимаем.

Запуск: python examples/saturday_afternoon_settle_pommel.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, опирается на луку",
        backstory="Суббота 10 октября, после поглаживания луки ладонью, седло ждёт тихого опоры",
    )
    print(dragon.stroke_pommel("луку после полудня после нюзла"))
    print()
    print(dragon.settle_pommel("луку после поглаживания"))
    print()
    print(dragon.talk("Опрись на луку над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
