"""К середине дня 8 октября: край попоны на согретые петли, седло не снимаем.

Запуск: python examples/thursday_drape_loops.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, не развязывает узелок",
        backstory="К середине дня 8 октября дыхание уже лежит на Мёде, Шве и Седле",
    )
    print(dragon.warm_loops("дыхание на петлях медового узелка к позднему дню"))
    print()
    print(dragon.drape_loops("край попоны на петлях медового узелка к середине дня"))
    print()
    print(dragon.talk("Накрой петли узелка над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
