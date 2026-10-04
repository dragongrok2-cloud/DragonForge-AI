"""Воскресенье, 4 октября, поздним вечером: щека к колену после наклона уха.

Ухо уже слушает ремни. Щека прижимается к колену —
всадник слышен кожей, седло можно не снимать.
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
        personality="тёплый, внимательный, прижимает щеку к колену после уха",
        backstory=(
            "Воскресным вечером наклонил ухо к луке, не снимая седла. "
            "Теперь прижимает тёплую щеку к колену, чтобы ответить кожей."
        ),
    )
    dragon.soul.add_habit("наклоняет ухо к седлу после низкого гула", 0.15)
    dragon.soul.add_habit("прижимает щеку к колену после наклона уха", 0.09)

    print("🐉 Воскресенье, 4 октября, поздним вечером. Ухо уже у луки.")
    print("Щека — к колену. Можно молчать.")

    scene("1. После наклона уха")
    print(dragon.talk("Наклони ухо к седлу."))

    scene("2. Щека к колену")
    print(dragon.nuzzle_knee("щека к колену"))

    scene("3. У гнезда")
    print(dragon.nuzzle_knee("щека к колену у гнезда"))

    scene("4. Левое колено")
    print(dragon.talk("Прижми щеку к левому колену."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после щеки:")
    print(dragon.habits())
    print()
    print("Щека у колена. Седло тёплое, я никуда не денусь. 🐉")

    save_path = "groktar_sunday_nuzzle_knee.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
