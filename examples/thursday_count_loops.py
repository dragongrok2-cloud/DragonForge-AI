"""Четверг, 8 октября, позднее утро: петли медового узелка."""

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
        personality="заботливый, к позднему утру считает петли и не развязывает узелок",
        backstory=(
            "К позднему утру 8 октября ухо уже слушало медовый узелок. "
            "Дракон только считает петли, не снимая седла."
        ),
    )
    dragon.soul.add_habit("слушает медовый узелок утром", 0.46)

    print("🐉 Четверг, 8 октября, позднее утро. Шов уже послушали, свет мягкий.")
    print("Узелок не развязываем. Седло не снимаем.")

    scene("1. Утреннее ухо ещё помнится")
    print(dragon.listen_knot("ухо к медовому узелку утром"))

    scene("2. Три тихие петли")
    print(dragon.count_loops("петли медового узелка к позднему утру"))

    scene("3. Левая сторона после уха")
    print(dragon.talk("Посчитай петли левого узелка. Поворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Сколько петель на узелке над рекой? Седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после позднего утра:")
    print(dragon.habits())
    print()
    print("Петли на месте, ремни держат. Лети со мной, всадник. 🍯")

    save_path = "grok_thursday_count_loops.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
