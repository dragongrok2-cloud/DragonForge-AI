"""Суббота, 3 октября: после росы подтянуть подпругу."""

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
        personality="заботливый, внимательный к ремням, уже не сонный",
        backstory=(
            "Росу с луки седла уже смахнул. Перед субботним кругом "
            "проверяет подпругу: после сырости она чуть ослабла."
        ),
    )
    dragon.soul.add_habit("смахивает утреннюю росу с седла", 0.4)
    dragon.soul.add_habit("подтягивает подпругу после росы", 0.28)

    print("🐉 Суббота, 3 октября. Седло сухое, пряжка ещё свободная.")
    print("Выходной круг подождёт одну дырочку.")

    scene("1. После росы")
    print(dragon.talk("Роса смахнута. Подтяни подпругу, пожалуйста."))

    scene("2. На одну дырочку")
    print(dragon.cinch_girth("на одну дырочку"))

    scene("3. Чуть-чуть, если ещё болтается")
    print(dragon.cinch_girth("чуть-чуть, только чтобы не болталась"))

    scene("4. Короткий круг")
    print(dragon.talk("Подпруга на месте. Можно невысоко над рекой."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после подпруги:")
    print(dragon.habits())
    print()
    print("Седло не сползёт. Садись, всадник. 🪢")

    save_path = "groktar_saturday_cinch_girth.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
