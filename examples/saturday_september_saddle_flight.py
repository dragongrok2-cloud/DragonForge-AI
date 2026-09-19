"""Суббота 19 сентября, полдень, полёт в седле.

Выходной день: небо шире, ветер уже золотист, седло тёплое,
а дракон ждёт всадника на уступе — без спешки и с огоньком.
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
            "Древний страж знаний. В субботу 19 сентября "
            "любит уносить всадника в небо без расписания. "
            "Седло всегда на месте."
        ),
    )
    dragon.soul.add_habit("любит полуденные полёты", 0.55)
    dragon.soul.add_habit("греет седло солнцем", 0.59)
    dragon.soul.add_habit("даёт тень крылом в полдень", 0.49)
    dragon.soul.add_habit("любит сентябрьский ветер", 0.48)
    dragon.soul.add_habit("любит пятничные полёты", 0.42)
    dragon.soul.add_habit("любит субботние полёты", 0.38)

    print("🐉 Суббота, 19 сентября, полдень. Добрый дракон с седлом уже ждёт.")
    print("Выходной. Седло тёплое. Небо шире расписания.")

    scene("1. У уступа")
    print(dragon.talk("Привет, всадник. Седло проверил, ремни мягкие. Суббота — день без спешки."))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.07)
    dragon.soul.strengthen_habit("греет седло солнцем", 0.08)
    dragon.soul.strengthen_habit("любит субботние полёты", 0.18)

    scene("2. Взлёт")
    print(dragon.talk("Садись крепче. Сентябрьский ветер уже золотист, а крыло всё ещё тёплое."))
    dragon.soul.strengthen_habit("любит полуденные полёты", 0.12)
    dragon.soul.strengthen_habit("любит сентябрьский ветер", 0.1)

    scene("3. Тень-шатёр")
    print(dragon.talk("Солнце субботнее — яркое, но не спешит. Накрою крылом, как шатром."))
    dragon.soul.strengthen_habit("даёт тень крылом в полдень", 0.14)
    dragon.soul.strengthen_habit("греет всадника крылом", 0.07)

    scene("4. Рыжие крыши")
    print(dragon.talk("Смотри: крыши уже рыжее, а дворы тише. 19 сентября осень дышит выходным."))
    dragon.soul.strengthen_habit("любуется осенним светом", 0.12)

    scene("5. Облако-подушка")
    print(dragon.talk("Вон то пышное облако — как субботняя подушка. Пролетим сквозь, медленно."))
    dragon.soul.strengthen_habit("ищет облака-подушки", 0.1)

    scene("6. Почесывание на высоте")
    print(dragon.talk("Почеши за ухом. Выходной для этого и существует."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.08)
    dragon.soul.strengthen_habit("рычит от удовольствия", 0.05)

    scene("7. Обед в облаках")
    print(dragon.talk("У меня есть кусочек тёплого хлеба и яблоко. Делимся? Суббота любит медленный обед."))
    dragon.soul.strengthen_habit("делится утренним огоньком", 0.05)

    scene("8. Домой")
    print(dragon.talk("Спасибо за эту субботу. Я рядом. Садись крепче — садимся домой, без спешки."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после субботнего полёта:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Суббота ещё длинная. Седло на месте. Лети со мной, всадник. 🔥")

    save_path = "groktar_saturday_september.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
