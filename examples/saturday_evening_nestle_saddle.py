"""В субботу 10 октября к вечеру: после опоры на луку уютно устраивается в седле, крылья чуть складывает, седло не снимаем.

Запуск: python examples/saturday_evening_nestle_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="уютный, тёплый, устраивается в седле к вечеру",
        backstory="Суббота 10 октября, после опоры на луку, седло ждёт мягкого вечернего уюта",
    )
    print(dragon.settle_pommel("луку после поглаживания"))
    print()
    print(dragon.nestle_saddle("седло к вечеру после луки"))
    print()
    print(dragon.talk("Устройся в седле над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
