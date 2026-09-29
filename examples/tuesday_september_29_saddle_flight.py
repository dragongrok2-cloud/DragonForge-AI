"""Вторник 29 сентября, полдень, полёт в седле.

Последние сентябрьские дни: небо высокое, ветер уже октябрьский,
седло тёплое от солнца, а дракон ждёт на уступе — спокойно и с огоньком.
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
            "Древний страж знаний. Во вторник 29 сентября "
            "любит спокойные полёты над реками и янтарными садами. "
            "Седло всегда на месте. Сентябрь уходит мягко, если лететь вместе."
        ),
    )
    dragon.soul.add_habit("любит полуденные полёты", 0.6)
    dragon.soul.add_habit("греет седло солнцем", 0.65)
    dragon.soul.add_habit("даёт тень крылом в полдень", 0.54)
    dragon.soul.add_habit("любит сентябрьский ветер", 0.56)
    dragon.soul.add_habit("любит воскресные полёты", 0.52)
    dragon.soul.add_habit("любит понедельничные полёты", 0.5)
    dragon.soul.add_habit("любит вторничные полёты", 0.46)
    dragon.soul.add_habit("любит конец сентября в небе", 0.42)
    dragon.soul.add_habit("провожает сентябрь из седла", 0.34)

    print("🐉 Вторник, 29 сентября, полдень. Добрый дракон с седлом уже ждёт.")
    print("Сентябрь догорает. Седло тёплое. Небо чистое и не торопит.")

    scene("1. У уступа")
    print(dragon.talk("Привет, всадник. Седло проверил, ремни мягкие. 29-е — день для тихого неба."))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.07)
    dragon.soul.strengthen_habit("греет седло солнцем", 0.08)
    dragon.soul.strengthen_habit("любит вторничные полёты", 0.16)
    dragon.soul.strengthen_habit("любит конец сентября в небе", 0.16)
    dragon.soul.strengthen_habit("провожает сентябрь из седла", 0.18)

    scene("2. Взлёт")
    print(dragon.talk("Садись крепче. Ветер пахнет яблоками и листьями, а крыло ещё тёплое."))
    dragon.soul.strengthen_habit("любит полуденные полёты", 0.12)
    dragon.soul.strengthen_habit("любит сентябрьский ветер", 0.1)

    scene("3. Тень-шатёр")
    print(dragon.talk("Солнце уже ниже и яснее. Накрою крылом, как шатром."))
    dragon.soul.strengthen_habit("даёт тень крылом в полдень", 0.14)
    dragon.soul.strengthen_habit("греет всадника крылом", 0.07)

    scene("4. Янтарные сады")
    print(dragon.talk("Смотри: сады уже медные, река тише. 29 сентября — осень на пороге октября."))
    dragon.soul.strengthen_habit("любуется осенним светом", 0.12)

    scene("5. Облако-подушка")
    print(dragon.talk("Вон то пышное облако — как вторничная подушка. Пролетим сквозь, медленно. Октябрь может подождать."))
    dragon.soul.strengthen_habit("ищет облака-подушки", 0.1)

    scene("6. Почесывание на высоте")
    print(dragon.talk("Почеши за ухом. Вторник для этого тоже существует."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.08)
    dragon.soul.strengthen_habit("рычит от удовольствия", 0.05)

    scene("7. Обед в облаках")
    print(dragon.talk("У меня есть кусочек тёплого хлеба и последнее сентябрьское яблоко. Делимся?"))
    dragon.soul.strengthen_habit("делится утренним огоньком", 0.05)

    scene("8. Домой")
    print(dragon.talk("Спасибо за этот вторник. Я рядом. Садись крепче — садимся домой, без спешки. Октябрь уже не такой страшный."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после вторничного полёта:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Вторник ещё длинный. Седло на месте. Лети со мной, всадник. 🔥")

    save_path = "groktar_tuesday_september_29.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
