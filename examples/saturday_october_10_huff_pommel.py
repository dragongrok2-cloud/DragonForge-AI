"""Утром 10 октября: тёплый выдох на луку после обвода, седло не снимаем.

Запуск: python examples/saturday_october_10_huff_pommel.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, дышит на луку утром",
        backstory="Утром 10 октября тепло ещё держится после обвода луки когтем",
    )
    print(dragon.trace_pommel("луку утром после глажки"))
    print()
    print(dragon.huff_pommel("луку утром после обвода"))
    print()
    print(dragon.talk("Дышни на луку утром"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
