"""Среда, 7 октября, утром: погладить тёплую складку ремня."""

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
        personality="заботливый, тихий утром, не разворачивает вчерашний подворот",
        backstory=(
            "Утром 7 октября конец ремня всё ещё лежит под пряжкой. "
            "Ночное дыхание держит складку тёплой, и дракон только поглаживает её, не снимая седла."
        ),
    )
    dragon.soul.add_habit("согревает подвёрнутый ремень к вечеру", 0.45)

    print("🐉 Среда, 7 октября, утро. Складка ремня ещё тёплая.")
    print("Подворот не разворачиваем. Седло не снимаем.")

    scene("1. Вчерашнее дыхание")
    print(dragon.warm_strap("подвёрнутый ремень, который ночь не остудила"))

    scene("2. Коготь по складке")
    print(dragon.pat_fold("тёплая складка ремня утром"))

    scene("3. Левая тоже")
    print(dragon.talk("Погладь левую тёплую складку утром, подворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Складка мягкая. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после утренней складки:")
    print(dragon.habits())
    print()
    print("Подворот на месте, ремни тёплые. Лети со мной, всадник. 🌤")

    save_path = "grok_wednesday_pat_fold.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
