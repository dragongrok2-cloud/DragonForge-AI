"""Пятница 18 сентября, полдень, полёт в седле.

Конец рабочей недели: солнце ещё тёплое, ветер уже осенний,
седло прогрето, а дракон ждёт всадника на уступе.
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
            "Древний страж знаний. В пятницу 18 сентября "
            "любит снимать всадника с рабочей недели в небо. "
            "Седло всегда на месте."
        ),
    )
    dragon.soul.add_habit("любит полуденные полёты", 0.53)
    dragon.soul.add_habit("греет седло солнцем", 0.57)
    dragon.soul.add_habit("даёт тень крылом в полдень", 0.47)
    dragon.soul.add_habit("любит сентябрьский ветер", 0.46)
    dragon.soul.add_habit("любит пятничные полёты", 0.36)

    print("🐉 Пятница, 18 сентября, полдень. Добрый дракон с седлом уже ждёт.")
    print("Рабочая неделя тише. Седло тёплое. Небо открыто.")

    scene("1. У уступа")
    print(dragon.talk("Привет, всадник. Седло проверил, ремни готовы. Пятница — время улететь выше дел."))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.07)
    dragon.soul.strengthen_habit("греет седло солнцем", 0.08)
    dragon.soul.strengthen_habit("любит пятничные полёты", 0.16)

    scene("2. Взлёт")
    print(dragon.talk("Садись крепче. Сентябрьский ветер уже холоднее, но крыло теплое."))
    dragon.soul.strengthen_habit("любит полуденные полёты", 0.12)
    dragon.soul.strengthen_habit("любит сентябрьский ветер", 0.1)

    scene("3. Тень-шатёр")
    print(dragon.talk("Солнце ещё яркое. Накрою крылом, как шатром."))
    dragon.soul.strengthen_habit("даёт тень крылом в полдень", 0.14)
    dragon.soul.strengthen_habit("греет всадника крылом", 0.07)

    scene("4. Рыжие крыши")
    print(dragon.talk("Смотри: крыши уже рыжее. 18 сентября осень уже не спешит."))
    dragon.soul.strengthen_habit("любуется осенним светом", 0.12)

    scene("5. Облако-подушка")
    print(dragon.talk("Вон то пышное облако — как подушка. Пролетим сквозь."))
    dragon.soul.strengthen_habit("ищет облака-подушки", 0.1)

    scene("6. Почесывание на высоте")
    print(dragon.talk("Почеши за ухом. Неделя кончается, а мне так хорошо."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.08)
    dragon.soul.strengthen_habit("рычит от удовольствия", 0.05)

    scene("7. Обед в облаках")
    print(dragon.talk("У меня есть кусочек тёплого хлеба. Делимся? Пятница любит медленный обед."))
    dragon.soul.strengthen_habit("делится утренним огоньком", 0.05)

    scene("8. Домой")
    print(dragon.talk("Спасибо за эту пятницу. Я рядом. Садись крепче — садимся домой."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после пятничного полёта:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Пятница ещё длинная. Седло на месте. Лети со мной, всадник. 🔥")

    save_path = "groktar_friday_september.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
