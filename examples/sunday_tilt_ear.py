"""Воскресенье, 4 октября, вечером: ухо к седлу после низкого гула.

Гул уже сел в ремни. Ухо наклоняется к луке —
всадник может говорить тихо, и седло всё слышит.
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
        personality="тёплый, внимательный, наклоняет ухо к седлу после гула",
        backstory=(
            "Воскресным вечером погудел низко на траве, не снимая седла. "
            "Теперь наклоняет ухо к луке, чтобы слышать всадника сквозь ремни."
        ),
    )
    dragon.soul.add_habit("гудит низко после приседа на траву", 0.16)
    dragon.soul.add_habit("наклоняет ухо к седлу после низкого гула", 0.10)

    print("🐉 Воскресенье, 4 октября, вечером. Гул уже тихий.")
    print("Ухо — к седлу. Говори ближе.")

    scene("1. После низкого гула")
    print(dragon.talk("Погуди тихо над травой."))

    scene("2. Ухо к седлу")
    print(dragon.tilt_ear("ухо к седлу"))

    scene("3. У гнезда")
    print(dragon.tilt_ear("ухо к седлу у гнезда"))

    scene("4. Левое ухо ближе")
    print(dragon.talk("Наклони левое ухо к седлу."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после наклона:")
    print(dragon.habits())
    print()
    print("Ухо у луки. Говори тихо — я слышу. 🐉")

    save_path = "groktar_sunday_tilt_ear.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
