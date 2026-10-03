"""Суббота, 3 октября, после полудня: горизонт после облачной ягоды."""

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
        personality="смотрит далеко, спокойный после полудня, держит курс лапой",
        backstory=(
            "Росу смахнул, подпругу подтянул, стремена выровнял, поводья прогрел, "
            "ягодой поделился. Теперь можно показать горизонт."
        ),
    )
    dragon.soul.add_habit("делится облачной ягодой после поводьев", 0.40)
    dragon.soul.add_habit("указывает горизонт после ягоды", 0.22)

    print("🐉 Суббота, 3 октября, после полудня. Ладонь сладкая, линия неба чистая.")
    print("Короткий круг подождёт, пока я укажу курс.")

    scene("1. После ягоды")
    print(dragon.talk("Ягода сладкая. Укажи горизонт, пожалуйста."))

    scene("2. Запад")
    print(dragon.point_horizon("запад"))

    scene("3. Север")
    print(dragon.point_horizon("север"))

    scene("4. Короткий круг")
    print(dragon.talk("Вижу север. Можно невысоко над лугом."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после горизонта:")
    print(dragon.habits())
    print()
    print("Смотри туда. Я держу курс, всадник. 🌤️")

    save_path = "groktar_saturday_point_horizon.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
