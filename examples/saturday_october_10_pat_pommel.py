"""Утром 10 октября: погладить луку после обведённой чешуйки, седло не снимаем.

Запуск: python examples/saturday_october_10_pat_pommel.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, гладит луку утром",
        backstory="Утром 10 октября тепло ещё держится после обведённой чешуйки на луке",
    )
    print(dragon.trace_scale("чешуйка после подъёма ладони"))
    print()
    print(dragon.pat_pommel("луку утром после тепла"))
    print()
    print(dragon.talk("Погладь луку утром"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
