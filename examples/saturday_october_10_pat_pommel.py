"""Утром 10 октября: погладить луку после вчерашнего тепла, седло не снимаем.

Запуск: python examples/saturday_october_10_pat_pommel.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, гладит луку утром",
        backstory="Утром 10 октября тепло ещё держится на Мёде, Шве и Седле",
    )
    print(dragon.lay_warmth("тепло сгиба на луку к вечеру"))
    print()
    print(dragon.pat_pommel("луку утром после тепла"))
    print()
    print(dragon.talk("Погладь луку утром"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
