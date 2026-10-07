"""Среда, 7 октября, к позднему дню: дыхание на медовый узелок."""

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
        personality="заботливый, к позднему дню дышит на медовый узелок и не развязывает его",
        backstory=(
            "К позднему дню 7 октября узелок уже тихий на медовом хвостике. "
            "Дракон только согревает его коротким дыханием, не снимая седла."
        ),
    )
    dragon.soul.add_habit("завязывает узелок на медовом хвостике к позднему дню", 0.45)

    print("🐉 Среда, 7 октября, к позднему дню. Узелок уже завязан, воздух стынет.")
    print("Узелок не развязываем. Седло не снимаем.")

    scene("1. Узелок уже тихий")
    print(dragon.knot_thread("узелок на медовом хвостике к позднему дню"))

    scene("2. Короткое дыхание")
    print(dragon.huff_knot("дыхание на медовый узелок к позднему дню"))

    scene("3. Левая сторона")
    print(dragon.talk("Подыши на левый узелок, чтобы не стыл, подворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Согрей медовый узелок над рекой. Седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после дыхания:")
    print(dragon.habits())
    print()
    print("Узелок тёплый, ремни на месте. Лети со мной, всадник. 🍯")

    save_path = "grok_wednesday_huff_knot.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
