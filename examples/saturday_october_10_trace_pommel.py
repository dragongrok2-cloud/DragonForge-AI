"""Утром 10 октября: обвести луку после глажки, седло не снимаем.

Запуск: python examples/saturday_october_10_trace_pommel.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, обводит луку утром",
        backstory="Утром 10 октября тепло ещё держится после глажки луки",
    )
    print(dragon.pat_pommel("луку утром после тепла"))
    print()
    print(dragon.trace_pommel("луку утром после глажки"))
    print()
    print(dragon.talk("Обведи луку утром"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
