"""Четверг, 8 октября, после полудня: тень крыла на названных петлях."""

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
        personality="заботливый, после полудня накрывает петли медового узелка тенью и не развязывает его",
        backstory=(
            "После полудня 8 октября петли уже названы: Мёд, Шов и Седло. "
            "Дракон только кладёт край крыла тенью, не снимая седла."
        ),
    )
    dragon.soul.add_habit("называет петли медового узелка к раннему дню", 0.48)

    print("🐉 Четверг, 8 октября, после полудня. Петли названы, солнце уже выше шва.")
    print("Узелок не развязываем. Седло не снимаем.")

    scene("1. Три тихих имени ещё на месте")
    print(dragon.name_loops("имена петель медового узелка к раннему дню"))

    scene("2. Край крыла над узелком")
    print(dragon.shade_loops("тень крыла на петлях медового узелка после полудня"))

    scene("3. Левая сторона в тени")
    print(dragon.talk("Затени левые петли узелка. Поворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Накрой петли над рекой крылом. Седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после тени:")
    print(dragon.habits())
    print()
    print("Петли в тени, ремни на месте. Лети со мной, всадник. 🍯")

    save_path = "grok_thursday_shade_loops.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
