"""Суббота, 3 октября, к вечеру: отметить хребет после ровного планирования."""

from dragonforge import Character


def scene(title: str) -> None:
    print()
    print("─" * 56)
    print(title)
    print("─" * 56)


def main() -> None:
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="помнит изгибы земли и не теряет обратный путь",
        backstory=(
            "Росу смахнул, подпругу подтянул, стремена выровнял, поводья прогрел, "
            "ягодой поделился, указал горизонт, поймал термик и выровнял планирование. "
            "Теперь можно отметить хребет."
        ),
    )
    dragon.soul.add_habit("выравнивает планирование после термика", 0.35)
    dragon.soul.add_habit("отмечает хребет после планирования", 0.19)

    print("🐉 Суббота, 3 октября, к вечеру. Край ровный, даль ещё держит свет.")
    print("Короткий круг подождёт, пока я отмечу хребет.")

    scene("1. После планирования")
    print(dragon.talk("Планирование ровное. Отметь хребет над лугом."))

    scene("2. Дальний хребет")
    print(dragon.mark_ridge("дальний хребет над лугом"))

    scene("3. У излучины")
    print(dragon.mark_ridge("речной хребет у излучины"))

    scene("4. Облачная кромка")
    print(dragon.talk("Держусь за луку. Запомни хребет на облачной кромке."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после метки:")
    print(dragon.habits())
    print()
    print("Обратный путь не потеряется. Я уже помню изгиб, всадник. 🏔️")

    save_path = "groktar_saturday_mark_ridge.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
