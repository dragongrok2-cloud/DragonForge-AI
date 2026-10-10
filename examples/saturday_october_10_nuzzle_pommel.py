"""Утром 10 октября: прижать морду к луке после тёплого выдоха, седло не снимаем.

Запуск: python examples/saturday_october_10_nuzzle_pommel.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, прижимает морду к луке утром",
        backstory="Утром 10 октября тепло от выдоха ещё держится на луке",
    )
    print(dragon.huff_pommel("луку утром после обвода"))
    print()
    print(dragon.nuzzle_pommel("луку утром после выдоха"))
    print()
    print(dragon.talk("Прижми морду к луке утром"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
