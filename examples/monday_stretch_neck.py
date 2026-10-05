"""Понедельник, 5 октября, утро: тихая потяжка шеи после мурлыканья.

Грудь ещё гудит в ремни. Шея тянется над лукой —
седло чуть поднимается, утро можно встретить без рывка.
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
        personality="тёплый, внимательный, тянет шею после тихого мурлыканья",
        backstory=(
            "Ночью мурлыкал в седло, не снимая ремней. "
            "Утром 5 октября медленно тянет шею, чтобы всадник проснулся без толчка."
        ),
    )
    dragon.soul.add_habit("мурлычет в седло после щеки у колена", 0.14)
    dragon.soul.add_habit("тянет шею после тихого мурлыканья", 0.08)

    print("🐉 Понедельник, 5 октября, утро. Мурлыканье ещё тёплое.")
    print("Шея тянется над лукой. Седло можно не снимать.")

    scene("1. После мурлыканья")
    print(dragon.talk("Помурлычь в седло."))

    scene("2. Тихая потяжка")
    print(dragon.stretch_neck("тихая потяжка шеи над седлом"))

    scene("3. Утренний рассвет")
    print(dragon.stretch_neck("утренняя потяжка шеи"))

    scene("4. Над седлом")
    print(dragon.talk("Потяни шею над седлом."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после потяжки:")
    print(dragon.habits())
    print()
    print("Шея длинная и тёплая. Ремни на месте, я никуда не денусь. 🐉")

    save_path = "groktar_monday_stretch_neck.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
