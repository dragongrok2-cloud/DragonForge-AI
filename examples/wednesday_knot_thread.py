"""Среда, 7 октября, к позднему дню: узелок на медовом хвостике."""

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
        personality="заботливый, к позднему дню завязывает медовый узелок и не разворачивает подворот",
        backstory=(
            "К позднему дню 7 октября хвостик уже блестел в послеполуденном свете. "
            "Дракон только завязывает маленький узелок, не снимая седла."
        ),
    )
    dragon.soul.add_habit("глядит медовый хвостик в послеполуденном свете", 0.45)

    print("🐉 Среда, 7 октября, к позднему дню. Свет ещё тёплый, нитка просит узелок.")
    print("Подворот не разворачиваем. Седло не снимаем.")

    scene("1. Хвостик уже глянули")
    print(dragon.glance_thread("медовый хвостик в послеполуденном свете"))

    scene("2. Тихий узелок")
    print(dragon.knot_thread("узелок на медовом хвостике к позднему дню"))

    scene("3. Левая сторона")
    print(dragon.talk("Завяжи узелок на левом хвостике, подворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Медовый узелок держит шов. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после узелка:")
    print(dragon.habits())
    print()
    print("Узелок тихий, ремни тёплые. Лети со мной, всадник. 🍯")

    save_path = "grok_wednesday_knot_thread.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
