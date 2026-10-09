"""В полдень 9 октября: яблочная крошка на полоске солнца, седло не снимаем.

Запуск: python examples/friday_noon_share_crumb.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, делит полдень пополам",
        backstory="К полудню 9 октября полоска солнца уже легла на сухое стекло на Мёде, Шве и Седле",
    )
    print(dragon.tilt_glass("полоска солнца на сухом стекле к одиннадцати"))
    print()
    print(dragon.share_crumb("яблочная крошка на полоске солнца в полдень"))
    print()
    print(dragon.talk("Поделись крошкой над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
