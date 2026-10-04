"""Воскресенье, 4 октября, после полудня: тёплый выдох после моргания.

Веко уже поднялось. К полудню морда дышит на перчатки —
седло помнит, что пальцы не должны стынуть.
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
        personality="тёплый, терпеливый, дышит на перчатки после моргания",
        backstory=(
            "Воскресным полуднем медленно моргнул, не снимая морды с луки. "
            "Теперь выдыхает тепло на перчатки, чтобы всадник держал поводья спокойно."
        ),
    )
    dragon.soul.add_habit("медленно моргает после морды на луке", 0.28)
    dragon.soul.add_habit("дышит теплом после медленного моргания", 0.14)

    print("🐉 Воскресенье, 4 октября, после полудня. Веко уже поднялось.")
    print("Короткий круг подождёт, пока я дыхну на перчатки.")

    scene("1. После медленного моргания")
    print(dragon.talk("Моргни медленно."))

    scene("2. Тёплый выдох на перчатки")
    print(dragon.huff_warm("тёплый выдох на перчатки"))

    scene("3. Ладони")
    print(dragon.huff_warm("тёплый выдох на ладони"))

    scene("4. Поводья")
    print(dragon.talk("Подыши теплом на поводья."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после выдоха:")
    print(dragon.habits())
    print()
    print("Пальцы тёплые. Обопрись — я ещё дышу рядом. 🐉")

    save_path = "groktar_sunday_huff_warm.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
