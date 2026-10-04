"""Воскресенье, 4 октября: свернуть хвост после выбранного уступа.

Уступ уже выбран, утро тихое. Кольцо у луки держит седло, пока всадник
не проснулся до конца.
"""

from dragonforge import Character


def scene(title: str) -> None:
    print()
    print("─" * 56)
    print(title)
    print("─" * 56)


def main() -> None:
    dragon = Character(
        name="Грок",
        title="добрый дракон с седлом",
        personality="терпеливый, тёплый, помнит камни лучше карт",
        backstory=(
            "В субботу к вечеру отметил хребет и выбрал широкий уступ. "
            "Воскресным утром сворачивает хвост, чтобы седло не сползло."
        ),
    )
    dragon.soul.add_habit("выбирает уступ после хребта", 0.33)
    dragon.soul.add_habit("сворачивает хвост после уступа", 0.17)

    print("🐉 Воскресенье, 4 октября, утро. Уступ выбран, роса ещё на чешуе.")
    print("Короткий круг подождёт, пока я сверну хвост.")

    scene("1. После уступа")
    print(dragon.talk("Уступ выбран. Сверни хвост у луки."))

    scene("2. Кольцо у луки")
    print(dragon.coil_tail("кольцо у луки"))

    scene("3. У стремени")
    print(dragon.coil_tail("кольцо у стремени"))

    scene("4. Край камня")
    print(dragon.talk("Уложи хвост по краю уступа."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после кольца:")
    print(dragon.habits())
    print()
    print("Седло не сползёт. Я уже улёгся кольцом, всадник. 🐉")

    save_path = "groktar_sunday_coil_tail.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
