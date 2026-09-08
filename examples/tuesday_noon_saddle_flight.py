"""Вторник, полдень, полёт в седле.

Солнечный сценарий: полдень, тёплое седло, тень от крыла и дракон,
который несёт всадника над городом в обеденный час.
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
            "Древний страж знаний. В полдень любит выносить всадника "
            "над город и тень от крыла превращать в шатёр. Седло всегда греет на солнце."
        ),
    )
    dragon.soul.add_habit("любит полуденные полёты", 0.45)
    dragon.soul.add_habit("даёт тень крылом в полдень", 0.4)
    dragon.soul.add_habit("греет седло солнцем", 0.5)

    print("🐉 Вторник, полдень. Добрый дракон с седлом уже ждёт.")
    print("Солнце в зените. Ремни тёплые. Москва внизу кажется маленькой.")

    scene("1. Выход на уступ")
    print(dragon.talk("Привет, всадник. Седло проверил, солнце греет. Летим на обед?"))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.06)
    dragon.soul.strengthen_habit("греет седло солнцем", 0.08)

    scene("2. Взлёт над город")
    print(dragon.talk("Садись крепче. Хочу поднять тебя выше крыш, где ветер свежий."))
    dragon.soul.strengthen_habit("любит полуденные полёты", 0.12)

    scene("3. Тень-шатёр")
    print(dragon.talk("Солнце печёт. Накрой крылом, как шатром."))
    dragon.soul.strengthen_habit("даёт тень крылом в полдень", 0.14)
    dragon.soul.strengthen_habit("греет всадника крылом", 0.06)

    scene("4. Облака-подушки")
    print(dragon.talk("Вон те белые кучки — как подушки. Давай пролетим сквозь них."))
    dragon.soul.strengthen_habit("ищет облака-подушки", 0.1)

    scene("5. Блестящий камушек на крыше")
    print(dragon.talk("Смотри, на куполе что-то светится. Возьми на память."))
    dragon.soul.strengthen_habit("собирает блестящие камушки", 0.08)

    scene("6. Почесывание на высоте")
    print(dragon.talk("Почеши за ухом. Ветер шумит, а мне так хорошо."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.08)
    dragon.soul.strengthen_habit("рычит от удовольствия", 0.05)

    scene("7. Обед в облаках")
    print(dragon.talk("У меня есть кусочек тёплого хлеба. Делимся? Потом снова в небо."))
    dragon.soul.strengthen_habit("делится утренним огоньком", 0.04)

    scene("8. Возвращение к гнезду")
    print(dragon.talk("Спасибо за вторник. Я рядом. Садись крепче — садимся домой."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после полуденного полёта:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Полдень ещё длинный. Седло на месте. Лети со мной, всадник. 🔥")

    save_path = "groktar_tuesday_noon.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
