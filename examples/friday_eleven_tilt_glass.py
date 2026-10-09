"""К одиннадцати 9 октября: полоска солнца на сухом стекле, седло не снимаем.

Запуск: python examples/friday_eleven_tilt_glass.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, не вытаскивает фонарик",
        backstory="К одиннадцати 9 октября бусинка росы уже ушла со стекла на Мёде, Шве и Седле",
    )
    print(dragon.blot_bead("бусинка росы со стекла фонарика к середине утра"))
    print()
    print(dragon.tilt_glass("полоска солнца на сухом стекле к одиннадцати"))
    print()
    print(dragon.talk("Наклони стекло над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
