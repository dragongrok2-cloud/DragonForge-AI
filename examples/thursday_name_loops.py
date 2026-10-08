"""Четверг, 8 октября, к раннему дню: имена уже обведённых петель."""

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
        personality="заботливый, к раннему дню называет петли медового узелка и не развязывает его",
        backstory=(
            "К раннему дню 8 октября петли уже обведены когтем после полудня. "
            "Дракон только даёт им имена, не снимая седла."
        ),
    )
    dragon.soul.add_habit("обводит петли медового узелка к полудню", 0.46)

    print("🐉 Четверг, 8 октября, к раннему дню. Петли обведены, солнце ещё на шве.")
    print("Узелок не развязываем. Седло не снимаем.")

    scene("1. Коготь ещё помнит круг")
    print(dragon.trace_loops("коготь по петлям медового узелка к полудню"))

    scene("2. Три тихих имени")
    print(dragon.name_loops("имена петель медового узелка к раннему дню"))

    scene("3. Левая сторона в свете")
    print(dragon.talk("Назови левые петли узелка. Поворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Как зовут петли над рекой? Седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после имён:")
    print(dragon.habits())
    print()
    print("Петли по имени, ремни на месте. Лети со мной, всадник. 🍯")

    save_path = "grok_thursday_name_loops.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
