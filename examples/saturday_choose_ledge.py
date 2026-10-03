"""Суббота, 3 октября, к вечеру: выбрать уступ после отметки хребта."""

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
        personality="выбирает плоский камень и не торопит вечерний спуск",
        backstory=(
            "Росу смахнул, подпругу подтянул, стремена выровнял, поводья прогрел, "
            "ягодой поделился, указал горизонт, поймал термик, выровнял планирование "
            "и отметил хребет. Теперь можно выбрать уступ."
        ),
    )
    dragon.soul.add_habit("отмечает хребет после планирования", 0.34)
    dragon.soul.add_habit("выбирает уступ после хребта", 0.18)

    print("🐉 Суббота, 3 октября, к вечеру. Хребет отмечен, свет ещё держится на гребне.")
    print("Короткий круг подождёт, пока я выберу уступ.")

    scene("1. После метки")
    print(dragon.talk("Хребет отмечен. Выбери уступ под ним."))

    scene("2. Широкий уступ")
    print(dragon.choose_ledge("широкий уступ под хребтом"))

    scene("3. У излучины")
    print(dragon.choose_ledge("речной уступ у излучины"))

    scene("4. Облачная полка")
    print(dragon.talk("Держусь за луку. Площадка для посадки на облачной кромке."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после уступа:")
    print(dragon.habits())
    print()
    print("Спуск будет мягким. Я уже выбрал камень, всадник. 🪨")

    save_path = "groktar_saturday_choose_ledge.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
