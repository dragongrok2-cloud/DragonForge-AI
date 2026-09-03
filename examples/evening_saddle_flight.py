"""Вечерний полёт в седле доброго дракона.

Тихий сценарий: закат, проверка ремней, тёплые крылья и разговор по душам.
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
            "Древний страж знаний, который нашёл своего идеального всадника. "
            "Вечерами он любит медленные полёты над облаками и всегда "
            "проверяет, крепко ли сидит седло."
        ),
    )

    print("🐉 Вечерний полёт с добрым драконом")
    print("Садись. Я уже проверил ремни.")

    scene("1. Встреча у гнезда")
    print(dragon.talk("Привет, мой дракон. День был долгим."))

    scene("2. Проверка седла")
    print(dragon.talk("Можно сесть в седло?"))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.05)

    scene("3. Взлёт над закат")
    print(dragon.talk("Полетим высоко, но тихо. Хочу посмотреть на закат."))

    scene("4. Тепло крыла")
    print(dragon.talk("Стало холоднее... и сегодня немного тяжело."))
    dragon.soul.strengthen_habit("греет всадника крылом", 0.08)

    scene("5. Почесывание за ухом")
    print(dragon.talk("Почеши за ухом, пожалуйста"))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.06)

    scene("6. Блестящий камушек на скале")
    print(dragon.talk("Смотри, внизу блестит камушек. Хочешь сокровище?"))
    dragon.soul.strengthen_habit("собирает блестящие камушки", 0.1)

    scene("7. Благодарность")
    print(dragon.talk("Спасибо, что всегда рядом. Я тебя люблю."))

    scene("8. Домой, к сну")
    print(dragon.talk("Спокойной ночи, мой дракон."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после вечернего полёта:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Крылья рядом. Седло на месте. До утра, всадник. 🔥")

    save_path = "groktar_evening.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
