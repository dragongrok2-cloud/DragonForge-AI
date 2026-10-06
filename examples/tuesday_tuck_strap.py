"""Вторник, 6 октября, к вечеру: конец ремня после тихой пряжки."""

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
        personality="заботливый, тихий к вечеру, не снимает седло без просьбы",
        backstory=(
            "К вечеру 6 октября пряжка уже молчит. "
            "Свободный конец ремня ещё хлопает, и дракон подворачивает его когтем, не снимая седла."
        ),
    )
    dragon.soul.add_habit("прижимает пряжку после ровного стремени", 0.44)

    print("🐉 Вторник, 6 октября, к вечеру. Пряжка уже тихая.")
    print("Конец ремня хлопает. Седло не снимаем.")

    scene("1. Пряжка молчит")
    print(dragon.snug_buckle("пряжка после ровного стремени"))

    scene("2. Конец под пряжку")
    print(dragon.tuck_strap("конец ремня после тихой пряжки"))

    scene("3. Левый тоже")
    print(dragon.talk("Подогни левый конец ремня, чтобы не хлопал."))

    scene("4. Короткий круг без хлопков")
    print(dragon.talk("Ремень не хлопает. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после подвёрнутого конца:")
    print(dragon.habits())
    print()
    print("Хвост ремня под кожей, ремни на месте. Лети со мной, всадник. 🌤")

    save_path = "grok_tuesday_tuck_strap.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
