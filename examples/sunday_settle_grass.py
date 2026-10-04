"""Воскресенье, 4 октября, к вечеру: тихий присед после короткого круга.

Дуга уже замкнута. Крылья складываются над травой —
седло помнит, что луг держит обоих, и гнездо подождёт.
"""

from dragonforge import Character


def scene(title: str) -> None:
    print()
    print("─" * 56)
    print(title)
    print("─" * 56)


def main() -> None:
    dragon = Character(
        name="Грок",
        title="добрый дракон с седлом",
        personality="тёплый, терпеливый, садится на траву после короткого круга",
        backstory=(
            "Воскресным вечером замкнул короткую дугу над лугом, не снимая седла. "
            "Теперь опускается на мягкую траву, чтобы всадник слез, когда захочет."
        ),
    )
    dragon.soul.add_habit("делает короткий круг после тёплого выдоха", 0.27)
    dragon.soul.add_habit("опускается на траву после короткого круга", 0.12)

    print("🐉 Воскресенье, 4 октября, к вечеру. Дуга уже замкнута.")
    print("Луг подождёт нас обоих.")

    scene("1. После короткого круга")
    print(dragon.talk("Сделай короткий круг над лугом."))

    scene("2. Тихий присед на траву")
    print(dragon.settle_grass("мягкая трава у луга"))

    scene("3. У гнезда")
    print(dragon.settle_grass("трава у гнезда"))

    scene("4. Под хребтом")
    print(dragon.talk("Опустись на траву под хребтом."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после приседа:")
    print(dragon.habits())
    print()
    print("Когти едва касаются стеблей. Обопрись — я на траве. 🐉")

    save_path = "groktar_sunday_settle_grass.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
