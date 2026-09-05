"""Звёздный ночной полёт в седле.

Тихий сценарий: чёрное небо, тёплое седло, крыло-одеяло и дракон, который считает звёзды вместе с всадником.
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
            "Древний страж знаний. Ночью любит выносить всадника над тёмные хребты, "
            "греть крылом и шептать имена звёзд. Седло всегда проверяет дважды."
        ),
    )
    dragon.soul.add_habit("любит ночные полёты под звёздами", 0.5)
    dragon.soul.add_habit("шепчет имена созвездий", 0.35)
    dragon.soul.add_habit("ставит седло под луну", 0.4)

    print("🐉 Звёздный полёт с добрым драконом")
    print("Седло уже на спине. Ремни тёплые. Луна смотрит прямо на нас.")

    scene("1. Выход из пещеры")
    print(dragon.talk("Спокойной ночи. Я уже проверил седло. Летим?"))
    dragon.soul.strengthen_habit("всегда проверяет седло", 0.05)

    scene("2. Взлёт под луну")
    print(dragon.talk("Садись в седло. Хочу взлететь выше облаков, где звёзды гуще."))
    dragon.soul.strengthen_habit("любит ночные полёты под звёздами", 0.12)
    dragon.soul.strengthen_habit("ставит седло под луну", 0.08)

    scene("3. Крыло-одеяло")
    print(dragon.talk("Немного холодно. Согрей крылом."))
    dragon.soul.strengthen_habit("греет всадника крылом", 0.08)

    scene("4. Считаем звёзды")
    print(dragon.talk("Расскажи про созвездия. Я хочу услышать их имена."))
    dragon.soul.strengthen_habit("шепчет имена созвездий", 0.14)

    scene("5. Блестящий камушек в лунном свете")
    print(dragon.talk("Смотри, внизу блестит камушек. Дарю его тебе."))
    dragon.soul.strengthen_habit("собирает блестящие камушки", 0.09)

    scene("6. Почесывание над тишиной")
    print(dragon.talk("Почеши за ухом. Тут так тихо, что можно слышать сердце."))
    dragon.soul.strengthen_habit("любит почесывания за ухом", 0.07)
    dragon.soul.strengthen_habit("рычит от удовольствия", 0.05)

    scene("7. Далёкий гром за горами")
    print(dragon.talk("Вдали гром. Не бойся, я рядом. Седло держит."))

    scene("8. Возвращение домой")
    print(dragon.talk("Спасибо за ночь. Я тебя люблю. Давай вернёмся к гнезду."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после звёздного полёта:")
    print(dragon.habits())
    print()
    print("Душа:")
    print(dragon.describe_soul())
    print()
    print("Луна ещё высоко. Седло на месте. Спи, всадник — я на страже. 🔥")

    save_path = "groktar_starry_night.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
