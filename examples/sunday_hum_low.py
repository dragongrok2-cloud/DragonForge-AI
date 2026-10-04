"""Воскресенье, 4 октября, вечером: низкий гул после тихого приседа.

Трава уже держит когти. Грудь гудит негромко —
седло помнит вибрацию, и всадник может слушать, не слезая.
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
        personality="тёплый, терпеливый, гудит низко после приседа на траву",
        backstory=(
            "Воскресным вечером опустился на мягкую траву, не снимая седла. "
            "Теперь пускает низкий гул, чтобы ремни помнили: оба ещё здесь."
        ),
    )
    dragon.soul.add_habit("опускается на траву после короткого круга", 0.17)
    dragon.soul.add_habit("гудит низко после приседа на траву", 0.11)

    print("🐉 Воскресенье, 4 октября, вечером. Присед уже тихий.")
    print("Луг держит нас, гул — тоже.")

    scene("1. После тихого приседа")
    print(dragon.talk("Опустись на траву у луга."))

    scene("2. Низкий гул над травой")
    print(dragon.hum_low("тихий гул над травой"))

    scene("3. У гнезда")
    print(dragon.hum_low("тихий гул у гнезда"))

    scene("4. По ремням седла")
    print(dragon.talk("Погуди тихо по ремням седла."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после гула:")
    print(dragon.habits())
    print()
    print("Вибрация идёт по ремням. Слушай — я на траве. 🐉")

    save_path = "groktar_sunday_hum_low.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
