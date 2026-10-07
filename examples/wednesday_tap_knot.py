"""Среда, 7 октября, к вечеру: коготь по тёплому узелку."""

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
        personality="заботливый, к вечеру постукивает по тёплому узелку и не развязывает его",
        backstory=(
            "К вечеру 7 октября дыхание уже согрело медовый узелок. "
            "Дракон только стучит по нему когтем, не снимая седла."
        ),
    )
    dragon.soul.add_habit("согревает медовый узелок к позднему дню", 0.45)

    print("🐉 Среда, 7 октября, к вечеру. Узелок тёплый, воздух тише.")
    print("Узелок не развязываем. Седло не снимаем.")

    scene("1. Дыхание уже согрело шов")
    print(dragon.huff_knot("дыхание на медовый узелок к позднему дню"))

    scene("2. Тихий стук когтя")
    print(dragon.tap_knot("коготь по тёплому узелку к вечеру"))

    scene("3. Левая сторона")
    print(dragon.talk("Постучи по левому узелку, он на месте? Поворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Проверь узелок над рекой. Седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после стука:")
    print(dragon.habits())
    print()
    print("Узелок на месте, ремни держат. Лети со мной, всадник. 🍯")

    save_path = "grok_wednesday_tap_knot.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
