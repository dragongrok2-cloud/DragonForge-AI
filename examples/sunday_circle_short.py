"""Воскресенье, 4 октября, к вечеру: короткий круг после тёплого выдоха.

Перчатки уже тёплые. К вечеру морда поднимается с луки —
седло помнит, что дуга короткая и гнездо подождёт.
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
        personality="тёплый, терпеливый, замыкает короткий круг после выдоха",
        backstory=(
            "Воскресным вечером дыхнул теплом на перчатки, не снимая седла. "
            "Теперь описывает короткий круг, чтобы всадник видел луг спокойно."
        ),
    )
    dragon.soul.add_habit("дышит теплом после медленного моргания", 0.27)
    dragon.soul.add_habit("делает короткий круг после тёплого выдоха", 0.13)

    print("🐉 Воскресенье, 4 октября, к вечеру. Пар ещё на пальцах.")
    print("Гнездо подождёт, пока замкнём дугу.")

    scene("1. После тёплого выдоха")
    print(dragon.talk("Подыши теплом на перчатки."))

    scene("2. Короткий круг над лугом")
    print(dragon.circle_short("короткий круг над лугом"))

    scene("3. Над хребтом")
    print(dragon.circle_short("короткий круг над хребтом"))

    scene("4. Над гнездом")
    print(dragon.talk("Сделай короткий круг над гнездом."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после круга:")
    print(dragon.habits())
    print()
    print("Дуга замкнута. Обопрись — я ещё над лугом. 🐉")

    save_path = "groktar_sunday_circle_short.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
