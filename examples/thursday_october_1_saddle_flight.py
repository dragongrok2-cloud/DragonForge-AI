"""Четверг 1 октября, полдень, первый осенний полёт в седле.

Сентябрь уже поклонился. Небо яснее, ветер с хвоинкой,
седло тёплое от драконьей спины, а всадник встречает октябрь не с земли, а с высоты.
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
            "Древний страж знаний. В четверг 1 октября "
            "встречает новый месяц над золотыми кронами. "
            "Седло всегда на месте. Октябрь не страшен, если лететь вместе."
        ),
    )
    dragon.soul.add_habit("любит полуденные полёты", 0.64)
    dragon.soul.add_habit("греет седло солнцем", 0.66)
    dragon.soul.add_habit("даёт тень крылом в полдень", 0.55)
    dragon.soul.add_habit("любит четверговые полёты", 0.52)
    dragon.soul.add_habit("встречает октябрь из седла", 0.44)
    dragon.soul.add_habit("любит октябрьский ветер", 0.34)
    dragon.soul.add_habit("считает золотые кроны с высоты", 0.32)
    dragon.soul.add_habit("греет всадника крылом", 0.6)

    print("🐉 Четверг, 1 октября, полдень. Добрый дракон с седлом уже ждёт.")
    print("Первый день октября. Седло тёплое. Небо широкое и не торопит.")

    scene("1. У уступа")
    print(dragon.talk("Привет, всадник. Седло проверил, ремни мягкие. 1 октября — день, когда новый месяц кланяется с высоты."))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.07)
    dragon.soul.strengthen_habit("греет седло солнцем", 0.08)
    dragon.soul.strengthen_habit("любит четверговые полёты", 0.16)
    dragon.soul.strengthen_habit("встречает октябрь из седла", 0.2)
    dragon.soul.strengthen_habit("любит октябрьский ветер", 0.16)

    scene("2. Взлёт")
    print(dragon.talk("Садись крепче. Ветер пахнет хвоей и яблоками, а крыло уже тёплое."))
    dragon.soul.strengthen_habit("любит полуденные полёты", 0.12)
    dragon.soul.strengthen_habit("любит октябрьский ветер", 0.1)

    scene("3. Тень-шатёр")
    print(dragon.talk("Октябрьское солнце ясное, но уже не летнее. Накрою крылом, как шатром."))
    dragon.soul.strengthen_habit("даёт тень крылом в полдень", 0.14)
    dragon.soul.strengthen_habit("греет всадника крылом", 0.08)

    scene("4. Золотые кроны")
    print(dragon.talk("Смотри: кроны уже золотые, река тише. 1 октября — осень начинается с неба, а не с календаря."))
    dragon.soul.strengthen_habit("считает золотые кроны с высоты", 0.18)
    dragon.soul.strengthen_habit("любуется осенним светом", 0.12)

    scene("5. Облако-подушка")
    print(dragon.talk("Вон то пышное облако — как первая октябрьская подушка. Пролетим сквозь, медленно."))
    dragon.soul.strengthen_habit("ищет облака-подушки", 0.1)

    scene("6. Почесывание на высоте")
    print(dragon.talk("Почеши за ухом. Первый октябрь для этого тоже существует."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.08)
    dragon.soul.strengthen_habit("рычит от удовольствия", 0.05)

    scene("7. Обед в облаках")
    print(dragon.talk("У меня есть кусочек тёплого хлеба и первое октябрьское яблоко. Делимся?"))
    dragon.soul.strengthen_habit("делится утренним огоньком", 0.05)

    scene("8. Домой")
    print(dragon.talk("Спасибо за этот первый октябрь. Я рядом. Садись крепче — садимся домой, без спешки."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после первого октябрьского полёта:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Октябрь уже в небе. Седло на месте. Лети со мной, всадник. 🔥")

    save_path = "groktar_thursday_october_1.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
