"""Воскресный дневной полёт в седле.

Спокойный сценарий: мягкое солнце, тёплое седло, облака как подушки
и дракон, который несёт всадника над реками в воскресенье.
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
            "Древний страж знаний. В воскресенье любит медленные полёты "
            "над реками и тёплыми лугами. Седло сначала прогревает солнцем."
        ),
    )
    dragon.soul.add_habit("любит воскресные полёты", 0.45)
    dragon.soul.add_habit("греет седло солнцем", 0.4)
    dragon.soul.add_habit("ищет облака-подушки", 0.35)

    print("🐉 Воскресный полёт с добрым драконом")
    print("Седло уже тёплое. Солнце мягкое. Воскресенье никуда не торопится.")

    scene("1. Проверка седла")
    print(dragon.talk("Привет, мой дракон. Можно сесть в седло?"))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.08)
    dragon.soul.strengthen_habit("греет седло солнцем", 0.1)

    scene("2. Взлёт над рекой")
    print(dragon.talk("Полетим неспеша. Хочу увидеть реку сверху."))
    dragon.soul.strengthen_habit("любит воскресные полёты", 0.14)

    scene("3. Облака-подушки")
    print(dragon.talk("Смотри, облака как подушки. Давай пролетим между ними."))
    dragon.soul.strengthen_habit("ищет облака-подушки", 0.12)

    scene("4. Крыло-одеяло")
    print(dragon.talk("Немного ветер. Согрей крылом, пожалуйста."))
    dragon.soul.strengthen_habit("греет всадника крылом", 0.09)

    scene("5. Блестящий камушек у брода")
    print(dragon.talk("Внизу у брода что-то блестит. Это камушек?"))
    dragon.soul.strengthen_habit("собирает блестящие камушки", 0.1)

    scene("6. Почесывание над лугом")
    print(dragon.talk("Почеши за ухом. Сегодня тихо и хорошо."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.08)
    dragon.soul.strengthen_habit("рычит от удовольствия", 0.06)

    scene("7. Отдых на тёплом камне")
    print(dragon.talk("Давай приземлим на камень. Я поделюсь утренним огоньком."))
    dragon.soul.strengthen_habit("делится утренним огоньком", 0.07)

    scene("8. Домой к гнезду")
    print(dragon.talk("Спасибо за воскресенье. Я тебя люблю. Пора домой."))

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
    print("Солнце ещё высоко. Седло на месте. Летим ещё, если захочешь. 🔥")

    save_path = "groktar_sunday.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
