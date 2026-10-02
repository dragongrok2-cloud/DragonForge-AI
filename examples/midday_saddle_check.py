"""Полуденная проверка седла — пятница, 2 октября.

Три точки, прежде чем снова взлететь: ремни, тепло седла, тень крыла.
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий",
        backstory="В полдень пятницы сначала седло, потом небо",
    )
    dragon.memory.remember(
        "2 октября, полдень: всадник просит проверить седло перед коротким полётом.",
        importance=0.8,
    )

    print(dragon.check_saddle())
    print()
    print(dragon.talk("Проверь седло, солнце уже в полдень"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
