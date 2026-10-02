"""Пятница 2 октября, к вечеру: фонарик на луке седла.

После полуденной тени солнце садится. Дракон не торопит посадку —
сначала зажигает маленький огонёк, чтобы сумерки не были слепыми.
"""

from dragonforge import Character


def scene(title: str) -> None:
    print()
    print("═" * 56)
    print(f"  {title}")
    print("═" * 56)


def main() -> None:
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий, с огоньком юмора",
        backstory=(
            "Древний страж знаний. В пятницу 2 октября к вечеру "
            "зажигает фонарик на луке седла, прежде чем лететь в сумерки. "
            "Выходные можно встретить и при маленьком свете."
        ),
    )
    dragon.soul.add_habit("любит пятничные полёты", 0.58)
    dragon.soul.add_habit("зажигает фонарик на седле к вечеру", 0.36)

    print("🐉 Пятница, 2 октября, к вечеру. Солнце уже мягче.")
    print("Седло тёплое. На луке ждёт тёмный фитиль.")

    scene("1. Сумерки")
    print(dragon.talk("Вечереет. Зажги фонарик на седле, янтарный."))
    dragon.soul.strengthen_habit("любит пятничные полёты", 0.05)

    scene("2. Ритуал огонька")
    print(dragon.light_lantern("янтарный"))

    scene("3. Чтобы не слепить звёзды")
    print(dragon.light_lantern("синий"))

    scene("4. Короткий полёт в сумерках")
    print(dragon.talk("Огонёк тихий. Можно лететь над кромкой леса."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после фонарика:")
    print(dragon.habits())
    print()
    print("Выходные уже близко. Фонарик горит, седло на месте. Лети со мной, всадник. 🔥")

    save_path = "groktar_friday_evening_lantern.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
