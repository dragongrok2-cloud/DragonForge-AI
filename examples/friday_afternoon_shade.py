"""Пятница 2 октября, после полудня: тень крыла над седлом.

Солнце ещё жёсткое, выходные уже близко. Дракон не садится сразу —
сначала накрывает всадника крылом и даёт коротко отдохнуть в седле.
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
            "Древний страж знаний. В пятницу 2 октября после полудня "
            "держит крыло над седлом, пока солнце не смягчится. "
            "Выходные можно встретить и в тени."
        ),
    )
    dragon.soul.add_habit("любит пятничные полёты", 0.55)
    dragon.soul.add_habit("даёт тень крылом после полудня", 0.4)

    print("🐉 Пятница, 2 октября, после полудня. Солнце ещё не сдалось.")
    print("Седло тёплое. Крыло уже готово стать навесом.")

    scene("1. Жёсткий свет")
    print(dragon.talk("Солнце печёт. Дай тень крыла, пожалуйста."))
    dragon.soul.strengthen_habit("любит пятничные полёты", 0.06)

    scene("2. Ритуал тени")
    print(dragon.offer_shade())

    scene("3. Короткий отдых")
    print(dragon.talk("После полудня можно не спешить. Я рядом."))
    dragon.soul.strengthen_habit("греет всадника крылом", 0.05)

    scene("4. Дальше, но спокойнее")
    print(dragon.talk("Тень была кстати. Можно лететь к золотым кронам."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после тени крыла:")
    print(dragon.habits())
    print()
    print("Выходные уже ближе. Крыло всё ещё над седлом. Лети со мной, всадник. 🔥")

    save_path = "groktar_friday_afternoon_shade.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
