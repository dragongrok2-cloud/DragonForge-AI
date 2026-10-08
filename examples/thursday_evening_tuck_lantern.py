"""К вечеру 8 октября: фонарик под разглаженный край попоны, седло не снимаем.

Запуск: python examples/thursday_evening_tuck_lantern.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, не развязывает узелок",
        backstory="К вечеру 8 октября край попоны уже разглажен на Мёде, Шве и Седле",
    )
    print(dragon.smooth_drape("край попоны на петлях медового узелка к вечеру"))
    print()
    print(dragon.tuck_lantern("фонарик под разглаженный край попоны к вечеру"))
    print()
    print(dragon.talk("Подсунь фонарик под край попоны над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
