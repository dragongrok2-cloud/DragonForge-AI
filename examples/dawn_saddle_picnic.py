"""Рассветный пикник в седле.

Тихий сценарий: раннее утро, тёплый огонёк, облако-стол и седло, которое дракон проверил ещё до солнца.
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
            "Древний страж знаний. Утрами любит выносить всадника над облака и "
            "делиться маленьким тёплым огоньком, пока солнце ещё ленивое."
        ),
    )
    dragon.soul.add_habit("любит рассветы над облаками", 0.55)
    dragon.soul.add_habit("делится утренним огоньком", 0.4)

    print("🐉 Рассветный пикник с добрым драконом")
    print("Седло уже тёплое. Я подыхал на ремни ещё до первой птицы.")

    scene("1. Просыпание у гнезда")
    print(dragon.talk("Доброе утро. Ещё рассвет, а я уже рядом."))

    scene("2. Проверка седла на рассвете")
    print(dragon.talk("Можно сесть в седло? Хочу взлететь к солнцу."))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.05)

    scene("3. Над розовыми облаками")
    print(dragon.talk("Полетим выше. Я люблю рассвет над облаками."))
    dragon.soul.strengthen_habit("любит рассветы над облаками", 0.12)

    scene("4. Утренний огонёк")
    print(dragon.talk("Немного холодно. Согрей крылом и дай огонёк."))
    dragon.soul.strengthen_habit("греет всадника крылом", 0.07)
    dragon.soul.strengthen_habit("делится утренним огоньком", 0.1)

    scene("5. Пикник на облаке")
    print(dragon.talk("Давай устроим пикник прямо на облаке. Я принёс чай."))

    scene("6. Почесывание и камушек в росе")
    print(dragon.talk("Почеши за ухом. И смотри, блестит камушек в росинке."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.06)
    dragon.soul.strengthen_habit("собирает блестящие камушки", 0.08)

    scene("7. Лёгкий дождь вдали")
    print(dragon.talk("Вдали дождь. Не боись, я рядом."))

    scene("8. Домой с благодарностью")
    print(dragon.talk("Спасибо за утро. Я тебя люблю."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после рассветного пикника:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Солнце встало. Седло на месте. Летим дальше, всадник. 🔥")

    save_path = "groktar_dawn.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
