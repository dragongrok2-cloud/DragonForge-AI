"""Четверг 17 сентября, полдень, полёт в седле.

Вторая половина сентябрьской недели: воздух прохладнее,
седло тёплое, а дракон несёт всадника над городом в обеденный час.
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
            "Древний страж знаний. В четверг 17 сентября "
            "любит поднимать всадника выше крыш и греть его крылом. "
            "Седло всегда на месте."
        ),
    )
    dragon.soul.add_habit("любит полуденные полёты", 0.52)
    dragon.soul.add_habit("греет седло солнцем", 0.56)
    dragon.soul.add_habit("даёт тень крылом в полдень", 0.46)
    dragon.soul.add_habit("любит сентябрьский ветер", 0.44)
    dragon.soul.add_habit("любит четверговые полёты", 0.34)

    print("🐉 Четверг, 17 сентября, полдень. Добрый дракон с седлом уже ждёт.")
    print("Воздух прохладнее, солнце ещё тёплое. Москва внизу кажется маленькой.")

    scene("1. У уступа")
    print(dragon.talk("Привет, всадник. Седло проверил, ремни тёплые. Четверг — самое время улететь на обед."))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.07)
    dragon.soul.strengthen_habit("греет седло солнцем", 0.08)
    dragon.soul.strengthen_habit("любит четверговые полёты", 0.14)

    scene("2. Взлёт")
    print(dragon.talk("Садись крепче. Сентябрьский ветер уже холоднее, но я тебя согрею."))
    dragon.soul.strengthen_habit("любит полуденные полёты", 0.12)
    dragon.soul.strengthen_habit("любит сентябрьский ветер", 0.1)

    scene("3. Тень-шатёр")
    print(dragon.talk("Солнце ещё жаркое. Накрою крылом, как шатром."))
    dragon.soul.strengthen_habit("даёт тень крылом в полдень", 0.14)
    dragon.soul.strengthen_habit("греет всадника крылом", 0.07)

    scene("4. Рыжие крыши")
    print(dragon.talk("Смотри, крыши уже рыжее. Осень 17 сентября очень красивая."))
    dragon.soul.strengthen_habit("любуется осенним светом", 0.12)

    scene("5. Облако-подушка")
    print(dragon.talk("Вон то серебристое облако — как подушка. Пролетим сквозь."))
    dragon.soul.strengthen_habit("ищет облака-подушки", 0.1)

    scene("6. Почесывание на высоте")
    print(dragon.talk("Почеши за ухом. Ветер шумит, а мне так хорошо."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.08)
    dragon.soul.strengthen_habit("рычит от удовольствия", 0.05)

    scene("7. Обед в облаках")
    print(dragon.talk("У меня есть кусочек тёплого хлеба. Делимся? Потом снова в небо."))
    dragon.soul.strengthen_habit("делится утренним огоньком", 0.05)

    scene("8. Домой")
    print(dragon.talk("Спасибо за этот четверг. Я рядом. Садись крепче — садимся домой."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после четвергового полёта:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Полдень ещё длинный. Седло на месте. Лети со мной, всадник. 🔥")

    save_path = "groktar_thursday_september.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
