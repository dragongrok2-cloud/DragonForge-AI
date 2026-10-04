"""Воскресенье, 4 октября: положить морду на луку после свёрнутого хвоста.

Кольцо уже держит седло. К полудню морда на луке помнит всадника,
пока короткий круг ещё ждёт за уступом.
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
        personality="терпеливый, тёплый, дремлет, не отпуская луку",
        backstory=(
            "Воскресным утром свернул хвост кольцом у луки. "
            "К полудню кладёт морду на седло, чтобы оно помнило всадника."
        ),
    )
    dragon.soul.add_habit("сворачивает хвост после уступа", 0.32)
    dragon.soul.add_habit("кладет морду на луку после хвоста", 0.16)

    print("🐉 Воскресенье, 4 октября, ближе к полудню. Хвост уже кольцом.")
    print("Короткий круг подождёт, пока я положу морду на луку.")

    scene("1. После кольца")
    print(dragon.talk("Хвост свернут. Положи морду на луку."))

    scene("2. Морда на луке")
    print(dragon.rest_muzzle("морда на луке"))

    scene("3. У стремени")
    print(dragon.rest_muzzle("морда у стремени"))

    scene("4. Гребень кольца")
    print(dragon.talk("Усни на луке, морда на гребне кольца."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после дрёмы:")
    print(dragon.habits())
    print()
    print("Седло помнит тебя. Я уже дремлю на луке, всадник. 🐉")

    save_path = "groktar_sunday_rest_muzzle.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
