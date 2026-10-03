"""Суббота, 3 октября, к вечеру: термик после указанного горизонта."""

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
        personality="держит курс, ловит тёплый столб без спешки",
        backstory=(
            "Росу смахнул, подпругу подтянул, стремена выровнял, поводья прогрел, "
            "ягодой поделился и указал горизонт. Теперь можно встать в термик."
        ),
    )
    dragon.soul.add_habit("указывает горизонт после ягоды", 0.40)
    dragon.soul.add_habit("ловит термик после горизонта", 0.21)

    print("🐉 Суббота, 3 октября, к вечеру. Курс виден, луг ещё тёплый.")
    print("Короткий круг подождёт, пока я поймаю подъём.")

    scene("1. После горизонта")
    print(dragon.talk("Горизонт вижу. Поймай термик над лугом."))

    scene("2. Тёплый столб")
    print(dragon.catch_thermal("тёплый столб над лугом"))

    scene("3. У скалы")
    print(dragon.catch_thermal("узкий столб у прогретой скалы"))

    scene("4. Выше луга")
    print(dragon.talk("Держусь за луку. Можно невысоко над полем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после термика:")
    print(dragon.habits())
    print()
    print("Держись за луку. Я не спешу, всадник. 🌤️")

    save_path = "groktar_saturday_catch_thermal.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
