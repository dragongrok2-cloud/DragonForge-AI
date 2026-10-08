"""Четверг, 8 октября, к полудню: коготь по посчитанным петлям."""

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
        personality="заботливый, к полудню обводит петли медового узелка и не развязывает его",
        backstory=(
            "К полудню 8 октября петли уже сосчитаны после утреннего уха. "
            "Дракон только обводит их когтем, не снимая седла."
        ),
    )
    dragon.soul.add_habit("считает петли медового узелка к позднему утру", 0.42)

    print("🐉 Четверг, 8 октября, к полудню. Петли сосчитаны, солнце на шве.")
    print("Узелок не развязываем. Седло не снимаем.")

    scene("1. Счёт ещё помнится")
    print(dragon.count_loops("петли медового узелка к позднему утру"))

    scene("2. Коготь по трём петлям")
    print(dragon.trace_loops("коготь по петлям медового узелка к полудню"))

    scene("3. Левая сторона в свете")
    print(dragon.talk("Обведи левые петли узелка. Поворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Проведи по петлям над рекой. Седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после полудня:")
    print(dragon.habits())
    print()
    print("Петли под когтем, ремни на месте. Лети со мной, всадник. 🍯")

    save_path = "grok_thursday_trace_loops.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
