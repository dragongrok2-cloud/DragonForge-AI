"""Среда, 7 октября, утром: посчитать стежки на тёплой складке."""

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
        personality="заботливый, тихий утром, считает стежки не разворачивая подворот",
        backstory=(
            "Утром 7 октября складка ремня ещё тёплая. "
            "Дракон гладит её и считает стежки, не снимая седла."
        ),
    )
    dragon.soul.add_habit("поглаживает тёплую складку ремня утром", 0.45)

    print("🐉 Среда, 7 октября, утро. Складка тёплая, стежки на месте.")
    print("Подворот не разворачиваем. Седло не снимаем.")

    scene("1. Погладить складку")
    print(dragon.pat_fold("тёплая складка ремня утром"))

    scene("2. Стежки у пряжки")
    print(dragon.count_stitch("стежки на тёплой складке утром"))

    scene("3. Левая сторона")
    print(dragon.talk("Посчитай стежки на левой складке, подворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Стежки целые. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после стежков:")
    print(dragon.habits())
    print()
    print("Шов держит, ремни тёплые. Лети со мной, всадник. 🌤")

    save_path = "grok_wednesday_count_stitch.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
