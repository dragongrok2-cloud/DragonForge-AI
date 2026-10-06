"""Вторник, 6 октября, полдень: тень крыла над лукой."""

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
        personality="заботливый, тихий в полдень, не снимает седло без просьбы",
        backstory=(
            "К полудню 6 октября роса уже с чешуйки снята, край попоны сложен под луку. "
            "Солнце садится на кожу седла, и дракон держит край крыла тенью."
        ),
    )
    dragon.soul.add_habit("складывает край попоны после росы", 0.4)

    print("🐉 Вторник, 6 октября, полдень. Попона сложена, лука греется.")
    print("Крыло не торопится в полёт. Сначала тень.")

    scene("1. Край попоны уже под лукой")
    print(dragon.fold_cloth("край попоны под лукой после росы"))

    scene("2. Тень над лукой")
    print(dragon.shade_pommel("тень крыла над лукой в полдень"))

    scene("3. Стремя тоже в тени")
    print(dragon.talk("Придержи крыло тенью над стременем, пожалуйста."))

    scene("4. Короткий круг без жары")
    print(dragon.talk("Лука в тени. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после полуденной тени:")
    print(dragon.habits())
    print()
    print("Лука прохладная, ремни на месте. Лети со мной, всадник. 🌤")

    save_path = "grok_tuesday_shade_pommel.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
