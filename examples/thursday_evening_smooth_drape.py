"""К вечеру 8 октября: ладонь по краю попоны, седло не снимаем.

Запуск: python examples/thursday_evening_smooth_drape.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, не развязывает узелок",
        backstory="К вечеру 8 октября край попоны уже лежит на Мёде, Шве и Седле",
    )
    print(dragon.drape_loops("край попоны на петлях медового узелка к середине дня"))
    print()
    print(dragon.smooth_drape("край попоны на петлях медового узелка к вечеру"))
    print()
    print(dragon.talk("Погладь край попоны над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
