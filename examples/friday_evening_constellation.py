"""Пятница 2 октября, вечер: шёпот созвездий над седлом.

Фонарик уже горит. Дракон не кричит в небо — называет звёзды тихо,
чтобы карта ночи легла рядом с ремнями.
"""

from dragonforge import Character


def scene(title: str) -> None:
    print()
    print("═" * 56)
    print(f"  {title}")
    print("═" * 56)


def main() -> None:
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий, с огоньком юмора",
        backstory=(
            "Древний страж знаний. В пятницу 2 октября вечером "
            "после фонарика шепчет имена созвездий. "
            "Выходные можно встретить и по звёздной карте."
        ),
    )
    dragon.soul.add_habit("любит пятничные полёты", 0.6)
    dragon.soul.add_habit("шепчет имена созвездий", 0.34)

    print("🐉 Пятница, 2 октября, вечер. Фонарик уже тёплый.")
    print("Седло держит. Небо над лукой начинает проступать.")

    scene("1. После огонька")
    print(dragon.talk("Фонарик тихий. Шепни звёзды, назови созвездие Лебедь."))
    dragon.soul.strengthen_habit("любит пятничные полёты", 0.04)

    scene("2. Ритуал карты")
    print(dragon.name_constellation("дракон"))

    scene("3. Корона над седлом")
    print(dragon.name_constellation("кассиопея"))

    scene("4. Короткий полёт по карте")
    print(dragon.talk("Карта неба с нами. Можно лететь вдоль реки."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после шёпота:")
    print(dragon.habits())
    print()
    print("Выходные уже близко. Созвездия названы, седло на месте. Лети со мной, всадник. ✨")

    save_path = "groktar_friday_evening_constellation.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
