"""Воскресенье, 4 октября: медленное моргание после морды на луке.

Морда уже лежит на седле. К полудню одно веко опускается —
знак, что я здесь и короткий круг может ещё подождать.
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
        personality="терпеливый, тёплый, моргает медленно, не снимая морды",
        backstory=(
            "Воскресным полуднем положил морду на луку. "
            "Теперь медленно моргает, чтобы седло знало: всадник не один."
        ),
    )
    dragon.soul.add_habit("кладет морду на луку после хвоста", 0.31)
    dragon.soul.add_habit("медленно моргает после морды на луке", 0.15)

    print("🐉 Воскресенье, 4 октября, ближе к полудню. Морда уже на луке.")
    print("Короткий круг подождёт, пока я моргну один раз.")

    scene("1. После дрёмы на луке")
    print(dragon.talk("Морда на луке. Моргни медленно."))

    scene("2. Медленное моргание")
    print(dragon.blink_slow("медленное моргание"))

    scene("3. Левый глаз")
    print(dragon.blink_slow("моргание левым глазом"))

    scene("4. Оба глаза")
    print(dragon.talk("Закрой глаз на миг — оба, знак глазом."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после моргания:")
    print(dragon.habits())
    print()
    print("Я здесь. Обопрись — веко уже поднялось. 🐉")

    save_path = "groktar_sunday_blink_slow.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
