"""Среда 30 сентября, полдень, полёт в седле.

Последний день сентября: небо высокое, ветер уже октябрьский,
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
            "Древний страж знаний. В среду 30 сентября "
            "любит тихие полёты над реками и медными садами. "
            "Седло всегда на месте. Сентябрь уходит мягко, если лететь вместе."
        ),
    )
    dragon.soul.add_habit("любит полуденные полёты", 0.62)
    dragon.soul.add_habit("греет седло солнцем", 0.67)
    dragon.soul.add_habit("даёт тень крылом в полдень", 0.56)
    dragon.soul.add_habit("любит сентябрьский ветер", 0.58)
    dragon.soul.add_habit("любит воскресные полёты", 0.52)
    dragon.soul.add_habit("любит понедельничные полёты", 0.5)
    dragon.soul.add_habit("любит вторничные полёты", 0.48)
    dragon.soul.add_habit("любит средненедельные полёты", 0.46)
    dragon.soul.add_habit("любит конец сентября в небе", 0.48)
    dragon.soul.add_habit("провожает сентябрь из седла", 0.42)
    dragon.soul.add_habit("встречает октябрь из седла", 0.3)

    print("🐉 Среда, 30 сентября, полдень. Добрый дракон с седлом уже ждёт.")
    print("Последний день сентября. Седло тёплое. Небо широкое и не торопит.")

    scene("1. У уступа")
    print(dragon.talk("Привет, всадник. Седло проверил, ремни мягкие. 30-е — день, когда сентябрь кланяется из неба."))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.07)
    dragon.soul.strengthen_habit("греет седло солнцем", 0.08)
    dragon.soul.strengthen_habit("любит средненедельные полёты", 0.16)
    dragon.soul.strengthen_habit("любит конец сентября в небе", 0.18)
    dragon.soul.strengthen_habit("провожает сентябрь из седла", 0.2)
    dragon.soul.strengthen_habit("встречает октябрь из седла", 0.16)

    scene("2. Взлёт")
    print(dragon.talk("Садись крепче. Ветер пахнет яблоками и дымком печей, а крыло ещё тёплое."))
    dragon.soul.strengthen_habit("любит полуденные полёты", 0.12)
    dragon.soul.strengthen_habit("любит сентябрьский ветер", 0.1)

    scene("3. Тень-шатёр")
    print(dragon.talk("Солнце последнего сентября — ясное и низкое. Накрою крылом, как шатром."))
    dragon.soul.strengthen_habit("даёт тень крылом в полдень", 0.14)
    dragon.soul.strengthen_habit("греет всадника крылом", 0.07)

    scene("4. Медные сады")
    print(dragon.talk("Смотри: сады уже медные, река тише. 30 сентября — осень на пороге октября."))
    dragon.soul.strengthen_habit("любуется осенним светом", 0.12)

    scene("5. Облако-подушка")
    print(dragon.talk("Вон то пышное облако — как прощальная сентябрьская подушка. Пролетим сквозь, медленно. Октябрь может подождать."))
    dragon.soul.strengthen_habit("ищет облака-подушки", 0.1)

    scene("6. Почесывание на высоте")
    print(dragon.talk("Почеши за ухом. Последний сентябрь для этого тоже существует."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.08)
    dragon.soul.strengthen_habit("рычит от удовольствия", 0.05)

    scene("7. Обед в облаках")
    print(dragon.talk("У меня есть кусочек тёплого хлеба и последнее сентябрьское яблоко. Делимся?"))
    dragon.soul.strengthen_habit("делится утренним огоньком", 0.05)

    scene("8. Домой")
    print(dragon.talk("Спасибо за этот последний сентябрь. Я рядом. Садись крепче — садимся домой, без спешки. Октябрь уже не такой страшный."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после средненедельного полёта:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Сентябрь ещё держится в небе. Седло на месте. Лети со мной, всадник. 🔥")

    save_path = "groktar_wednesday_september_30.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
