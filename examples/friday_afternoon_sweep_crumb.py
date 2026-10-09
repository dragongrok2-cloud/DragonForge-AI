"""После полудня 9 октября: крошка с полоски солнца, седло не снимаем.

Запуск: python examples/friday_afternoon_sweep_crumb.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, смахивает полдень крылом",
        backstory="После полудня 9 октября крошка уже лежала на полоске солнца на Мёде, Шве и Седле",
    )
    print(dragon.share_crumb("яблочная крошка на полоске солнца в полдень"))
    print()
    print(dragon.sweep_crumb("крошка с полоски солнца после полудня"))
    print()
    print(dragon.talk("Смахни крошку над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
