"""К вечеру 9 октября: тепло сгиба на луке, седло не снимаем.

Запуск: python examples/friday_evening_lay_warmth.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, кладёт тепло сгиба на луку",
        backstory="К вечеру 9 октября сгиб уже разжат на Мёде, Шве и Седле",
    )
    print(dragon.ease_fold("сгиб полоски солнца к вечеру"))
    print()
    print(dragon.lay_warmth("тепло сгиба на луке к вечеру"))
    print()
    print(dragon.talk("Положи тепло на луку к вечеру"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
