"""Среда, 7 октября, к позднему утру: назвать цвет нитки на стежках."""

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
        personality="заботливый, к позднему утру называет цвет нитки и не разворачивает подворот",
        backstory=(
            "К позднему утру 7 октября стежки уже посчитаны. "
            "Дракон называет цвет нитки, не снимая седла."
        ),
    )
    dragon.soul.add_habit("считает стежки на тёплой складке утром", 0.45)

    print("🐉 Среда, 7 октября, позднее утро. Стежки целые, нитка ещё тёплая.")
    print("Подворот не разворачиваем. Седло не снимаем.")

    scene("1. Стежки у пряжки")
    print(dragon.count_stitch("стежки на тёплой складке утром"))

    scene("2. Цвет нитки")
    print(dragon.name_thread("цвет нитки на стежках к позднему утру"))

    scene("3. Левая сторона")
    print(dragon.talk("Назови цвет нитки на левых стежках, подворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Нитка медовая. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после цвета нитки:")
    print(dragon.habits())
    print()
    print("Шов медовый, ремни тёплые. Лети со мной, всадник. 🌤")

    save_path = "grok_wednesday_name_thread.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
