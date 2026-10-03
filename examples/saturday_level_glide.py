"""Суббота, 3 октября, к вечеру: ровное планирование после термика."""

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
        personality="держит курс, выравнивает крылья без спешки",
        backstory=(
            "Росу смахнул, подпругу подтянул, стремена выровнял, поводья прогрел, "
            "ягодой поделился, указал горизонт и поймал термик. Теперь можно планировать ровно."
        ),
    )
    dragon.soul.add_habit("ловит термик после горизонта", 0.36)
    dragon.soul.add_habit("выравнивает планирование после термика", 0.20)

    print("🐉 Суббота, 3 октября, к вечеру. Подъём взят, луг ещё держит тепло.")
    print("Короткий круг подождёт, пока я выровняю крылья.")

    scene("1. После термика")
    print(dragon.talk("Термик взяли. Выровняй планирование над лугом."))

    scene("2. Ровный край")
    print(dragon.level_glide("ровный край над лугом"))

    scene("3. Над гребнем")
    print(dragon.level_glide("ровный гребень над тёплым склоном"))

    scene("4. Под облачной кромкой")
    print(dragon.talk("Держусь за луку. Можно глиссаду под облаками."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после планирования:")
    print(dragon.habits())
    print()
    print("Можно отпустить поводья на палец. Я не кренусь, всадник. 🌤️")

    save_path = "groktar_saturday_level_glide.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
