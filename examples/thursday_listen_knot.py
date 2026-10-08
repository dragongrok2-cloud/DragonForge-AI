"""Четверг, 8 октября, утро: ухо к медовому узелку."""

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
        personality="заботливый, утром слушает медовый узелок и не развязывает его",
        backstory=(
            "Утром 8 октября узелок переночевал на шве после вечернего стука. "
            "Дракон только прикладывает ухо, не снимая седла."
        ),
    )
    dragon.soul.add_habit("постукивает по тёплому узелку к вечеру", 0.46)

    print("🐉 Четверг, 8 октября, утро. Узелок переночевал, воздух ещё тихий.")
    print("Узелок не развязываем. Седло не снимаем.")

    scene("1. Вечерний стук ещё помнится")
    print(dragon.tap_knot("коготь по тёплому узелку к вечеру"))

    scene("2. Ухо к шву")
    print(dragon.listen_knot("ухо к медовому узелку утром"))

    scene("3. Левая сторона после ночи")
    print(dragon.talk("Послушай левый узелок за ночь. Поворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Послушай утренний узелок над рекой. Седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после утра:")
    print(dragon.habits())
    print()
    print("Узелок держит нитку, ремни на месте. Лети со мной, всадник. 🍯")

    save_path = "grok_thursday_listen_knot.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
