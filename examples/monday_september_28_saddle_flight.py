"""Понедельник 28 сентября, полдень, полёт в седле.

Конец сентября: небо высокое и прозрачное, ветер уже почти октябрьский,
седло прогрето, а дракон ждёт на уступе — без спешки, но с огоньком.
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
            "Древний страж знаний. В понедельник 28 сентября "
            "любит собранные полёты над реками и золотыми садами. "
            "Седло всегда на месте. Конец сентября не страшен, если лететь вместе."
        ),
    )
    dragon.soul.add_habit("любит полуденные полёты", 0.58)
    dragon.soul.add_habit("греет седло солнцем", 0.63)
    dragon.soul.add_habit("даёт тень крылом в полдень", 0.52)
    dragon.soul.add_habit("любит сентябрьский ветер", 0.54)
    dragon.soul.add_habit("любит воскресные полёты", 0.52)
    dragon.soul.add_habit("любит понедельничные полёты", 0.48)
    dragon.soul.add_habit("встречает новую неделю в седле", 0.44)
    dragon.soul.add_habit("любит конец сентября в небе", 0.36)

    print("🐉 Понедельник, 28 сентября, полдень. Добрый дракон с седлом уже ждёт.")
    print("Конец сентября. Седло тёплое. Небо прозрачное и не требует спешки.")

    scene("1. У уступа")
    print(dragon.talk("Привет, всадник. Седло проверил, ремни мягкие. 28-е — день для собранного неба."))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.07)
    dragon.soul.strengthen_habit("греет седло солнцем", 0.08)
    dragon.soul.strengthen_habit("любит понедельничные полёты", 0.16)
    dragon.soul.strengthen_habit("встречает новую неделю в седле", 0.14)
    dragon.soul.strengthen_habit("любит конец сентября в небе", 0.18)

    scene("2. Взлёт")
    print(dragon.talk("Садись крепче. Сентябрьский ветер уже пахнет яблоками и дымком от печей, а крыло ещё тёплое."))
    dragon.soul.strengthen_habit("любит полуденные полёты", 0.12)
    dragon.soul.strengthen_habit("любит сентябрьский ветер", 0.1)

    scene("3. Тень-шатёр")
    print(dragon.talk("Солнце конца сентября — ясное и низкое. Накрою крылом, как шатром."))
    dragon.soul.strengthen_habit("даёт тень крылом в полдень", 0.14)
    dragon.soul.strengthen_habit("греет всадника крылом", 0.07)

    scene("4. Золотые сады")
    print(dragon.talk("Смотри: сады уже янтарные, а река тише. 28 сентября осень уже почти октябрь."))
    dragon.soul.strengthen_habit("любуется осенним светом", 0.12)

    scene("5. Облако-подушка")
    print(dragon.talk("Вон то пышное облако — как понедельничная подушка. Пролетим сквозь, медленно. Октябрь может подождать."))
    dragon.soul.strengthen_habit("ищет облака-подушки", 0.1)

    scene("6. Почесывание на высоте")
    print(dragon.talk("Почеши за ухом. Понедельник для этого тоже существует."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.08)
    dragon.soul.strengthen_habit("рычит от удовольствия", 0.05)

    scene("7. Обед в облаках")
    print(dragon.talk("У меня есть кусочек тёплого хлеба и последнее сентябрьское яблоко. Делимся?"))
    dragon.soul.strengthen_habit("делится утренним огоньком", 0.05)

    scene("8. Домой")
    print(dragon.talk("Спасибо за этот понедельник. Я рядом. Садись крепче — садимся домой, без спешки. Октябрь уже не такой страшный."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после понедельничного полёта:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Понедельник ещё длинный. Седло на месте. Лети со мной, всадник. 🔥")

    save_path = "groktar_monday_september_28.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
