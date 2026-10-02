"""Пятница 2 октября, поздний вечер: разворот к гнезду.

Созвездия уже названы, фонарик тёплый. Дракон кренит крыло
и ведёт седло к огоньку дома, пока выходные ещё не сели на мох.
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
            "Древний страж знаний. В пятницу 2 октября поздним вечером "
            "после шёпота созвездий разворачивается к гнезду. "
            "Выходные можно встретить у тёплого огонька."
        ),
    )
    dragon.soul.add_habit("любит пятничные полёты", 0.6)
    dragon.soul.add_habit("разворачивается к гнезду к ночи", 0.32)

    print("🐉 Пятница, 2 октября, поздний вечер. Карта неба уже с нами.")
    print("Седло держит. Внизу мигает свой огонёк.")

    scene("1. После созвездий")
    print(dragon.talk("Карта неба с нами. Пора домой, к гнезду у реки."))
    dragon.soul.strengthen_habit("любит пятничные полёты", 0.04)

    scene("2. Ритуал разворота")
    print(dragon.bank_home("гнездо у реки"))

    scene("3. Запасная пещера")
    print(dragon.bank_home("пещера на утёсе"))

    scene("4. Короткий заход")
    print(dragon.talk("Гнездо ждёт. Можно снижаться по широкой спирали."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после разворота:")
    print(dragon.habits())
    print()
    print("Выходные уже близко. Нос к гнезду, седло на месте. Лети со мной, всадник. 🏠")

    save_path = "groktar_friday_evening_bank_home.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
