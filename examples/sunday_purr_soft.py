"""Воскресенье, 4 октября, к ночи: тихое мурлыканье после щеки у колена.

Щека уже греет колено. Грудь отвечает низким мурлыканьем —
седло и колено слышат, ремни можно не снимать.
"""

from dragonforge import Character


def scene(title: str) -> None:
    print()
    print("─" * 56)
    print(title)
    print("─" * 56)


def main() -> None:
    dragon = Character(
        name="Грок",
        title="добрый дракон с седлом",
        personality="тёплый, внимательный, мурлычет в седло после щеки у колена",
        backstory=(
            "Воскресным вечером прижал щеку к колену, не снимая седла. "
            "Теперь тихо мурлычет грудью, чтобы колено слышало ответ."
        ),
    )
    dragon.soul.add_habit("прижимает щеку к колену после наклона уха", 0.15)
    dragon.soul.add_habit("мурлычет в седло после щеки у колена", 0.09)

    print("🐉 Воскресенье, 4 октября, к ночи. Щека уже у колена.")
    print("Грудь мурлычет в ремни. Можно молчать.")

    scene("1. После щеки у колена")
    print(dragon.talk("Прижми щеку к колену."))

    scene("2. Тихое мурлыканье")
    print(dragon.purr_soft("тихое мурлыканье в седло"))

    scene("3. У гнезда")
    print(dragon.purr_soft("мурлыканье у гнезда"))

    scene("4. У колена")
    print(dragon.talk("Помурлычь у колена."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после мурлыканья:")
    print(dragon.habits())
    print()
    print("Грудь гудит теплом. Седло тёплое, я никуда не денусь. 🐉")

    save_path = "groktar_sunday_purr_soft.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
