"""Пятница, 2 октября, после полудня: короткий полёт и складывание крыльев.

Утренний полёт этого дня уже был. Теперь — мягкая посадка,
чтобы крылья отдохнули, а седло осталось на месте.
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="заботливый, спокойный после неба, не торопится",
        backstory="Утром уже летал с всадником. К полудню крылья тёплые, седло на месте.",
    )
    dragon.soul.add_habit("любит пятничные полёты", 0.48)

    print("=== Пятница, 2 октября — после полудня ===\n")
    print(dragon.talk("Привет. Короткий полёт после обеда?"))
    print()
    print(dragon.check_saddle())
    print()
    print(dragon.talk("Полетим над золотыми кронами, недалеко."))
    print()
    print(dragon.talk("Сложи крылья после полёта. Я слезу."))
    print()
    print(dragon.fold_wings())
    print()
    print(dragon.mood())
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
