"""Вторник, 6 октября, вечером: тёплый ремень после подворота."""

from dragonforge import Character


def scene(title: str) -> None:
    print()
    print("─" * 56)
    print(title)
    print("─" * 56)


def main() -> None:
    dragon = Character(
        name="Грок",
        title="Добрый дракон с седлом",
        personality="заботливый, тёплый к вечеру, не снимает седло без просьбы",
        backstory=(
            "Вечером 6 октября конец ремня уже лежит под пряжкой. "
            "Воздух стынет, и дракон греет складку коротким дыханием, не снимая седла."
        ),
    )
    dragon.soul.add_habit("подворачивает конец ремня после тихой пряжки", 0.45)

    print("🐉 Вторник, 6 октября, вечером. Конец ремня уже подвёрнут.")
    print("Кожа в складке стынет. Седло не снимаем.")

    scene("1. Конец под пряжку")
    print(dragon.tuck_strap("конец ремня после тихой пряжки"))

    scene("2. Дыхание на складку")
    print(dragon.warm_strap("подвёрнутый ремень к вечеру"))

    scene("3. Левый тоже")
    print(dragon.talk("Согрей левый подвёрнутый ремень, чтобы не стыл."))

    scene("4. Короткий круг без холодной кожи")
    print(dragon.talk("Ремень тёплый. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после тёплого ремня:")
    print(dragon.habits())
    print()
    print("Складка мягкая, ремни на месте. Лети со мной, всадник. 🌤")

    save_path = "grok_tuesday_warm_strap.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
