"""Вторник, 6 октября, после полудня: пряжка после ровного стремени."""

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
        personality="заботливый, тихий после полудня, не снимает седло без просьбы",
        backstory=(
            "После полудня 6 октября стремя уже ровное. "
            "Ветер ещё звенит пряжкой подпруги, и дракон прижимает её когтем, не снимая седла."
        ),
    )
    dragon.soul.add_habit("выравнивает стремя после опущенного края", 0.42)

    print("🐉 Вторник, 6 октября, после полудня. Стремя уже ровное.")
    print("Пряжка звенит. Седло не снимаем.")

    scene("1. Стремя после края")
    print(dragon.settle_stirrup("стремя после опущенного края"))

    scene("2. Пряжка тихо")
    print(dragon.snug_buckle("пряжка после ровного стремени"))

    scene("3. Левая тоже")
    print(dragon.talk("Прижми левую пряжку после стремени."))

    scene("4. Короткий круг без звона")
    print(dragon.talk("Пряжка молчит. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после тихой пряжки:")
    print(dragon.habits())
    print()
    print("Металл не звенит, ремни на месте. Лети со мной, всадник. 🌤")

    save_path = "grok_tuesday_snug_buckle.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
