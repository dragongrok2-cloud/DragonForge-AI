"""Воскресенье 20 сентября, полдень, полёт в седле.

Тихий выходной: небо высокое, ветер уже яблочный,
седло прогрето солнцем, а дракон ждёт на уступе без спешки.
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
            "Древний страж знаний. В воскресенье 20 сентября "
            "любит медленные полёты над реками и яблоневыми садами. "
            "Седло всегда на месте."
        ),
    )
    dragon.soul.add_habit("любит полуденные полёты", 0.56)
    dragon.soul.add_habit("греет седло солнцем", 0.61)
    dragon.soul.add_habit("даёт тень крылом в полдень", 0.50)
    dragon.soul.add_habit("любит сентябрьский ветер", 0.50)
    dragon.soul.add_habit("любит субботние полёты", 0.40)
    dragon.soul.add_habit("любит воскресные полёты", 0.52)

    print("🐉 Воскресенье, 20 сентября, полдень. Добрый дракон с седлом уже ждёт.")
    print("Выходной. Седло тёплое. Небо высокое и никуда не торопится.")

    scene("1. У уступа")
    print(dragon.talk("Привет, всадник. Седло проверил, ремни мягкие. Воскресенье — день для медленного неба."))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.07)
    dragon.soul.strengthen_habit("греет седло солнцем", 0.08)
    dragon.soul.strengthen_habit("любит воскресные полёты", 0.18)

    scene("2. Взлёт")
    print(dragon.talk("Садись крепче. Сентябрьский ветер уже пахнет яблоками, а крыло всё ещё тёплое."))
    dragon.soul.strengthen_habit("любит полуденные полёты", 0.12)
    dragon.soul.strengthen_habit("любит сентябрьский ветер", 0.1)

    scene("3. Тень-шатёр")
    print(dragon.talk("Солнце воскресное — мягкое и высокое. Накрою крылом, как шатром."))
    dragon.soul.strengthen_habit("даёт тень крылом в полдень", 0.14)
    dragon.soul.strengthen_habit("греет всадника крылом", 0.07)

    scene("4. Яблоневые сады")
    print(dragon.talk("Смотри: сады уже золотые, а река тише. 20 сентября осень дышит воскресеньем."))
    dragon.soul.strengthen_habit("любуется осенним светом", 0.12)

    scene("5. Облако-подушка")
    print(dragon.talk("Вон то пышное облако — как воскресная подушка. Пролетим сквозь, медленно."))
    dragon.soul.strengthen_habit("ищет облака-подушки", 0.1)

    scene("6. Почесывание на высоте")
    print(dragon.talk("Почеши за ухом. Воскресенье для этого и существует."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.08)
    dragon.soul.strengthen_habit("рычит от удовольствия", 0.05)

    scene("7. Обед в облаках")
    print(dragon.talk("У меня есть кусочек тёплого хлеба и яблоко. Делимся? Воскресенье любит медленный обед."))
    dragon.soul.strengthen_habit("делится утренним огоньком", 0.05)

    scene("8. Домой")
    print(dragon.talk("Спасибо за это воскресенье. Я рядом. Садись крепче — садимся домой, без спешки."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после воскресного полёта:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Воскресенье ещё длинное. Седло на месте. Лети со мной, всадник. 🔥")

    save_path = "groktar_sunday_september_20.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
