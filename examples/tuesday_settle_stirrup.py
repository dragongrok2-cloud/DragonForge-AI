"""Вторник, 6 октября, после полудня: стремя после опущенного края."""

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
            "После полудня 6 октября край крыла уже опущен после тени. "
            "Ветер качнул стремя, и дракон выравнивает его когтем, не снимая седла."
        ),
    )
    dragon.soul.add_habit("опускает край крыла после полуденной тени", 0.4)

    print("🐉 Вторник, 6 октября, после полудня. Край крыла уже ниже.")
    print("Стремя качнулось. Седло не снимаем.")

    scene("1. Край крыла после тени")
    print(dragon.ease_wing("край крыла после полуденной тени"))

    scene("2. Стремя ровно")
    print(dragon.settle_stirrup("стремя после опущенного края"))

    scene("3. Левое тоже")
    print(dragon.talk("Выровняй левое стремя после края крыла."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Стремя держит ногу. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после ровного стремени:")
    print(dragon.habits())
    print()
    print("Пряжка тихая, ремни на месте. Лети со мной, всадник. 🌤")

    save_path = "grok_tuesday_settle_stirrup.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()