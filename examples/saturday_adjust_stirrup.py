"""Суббота, 3 октября, полдень: выровнять стремена после подпруги."""

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
        personality="спокойный, внимательный к пяткам всадника, уже не сонный",
        backstory=(
            "Росу смахнул, подпругу подтянул. К полудню субботы "
            "стремена ещё чуть разной длины — левое ниже правого."
        ),
    )
    dragon.soul.add_habit("подтягивает подпругу после росы", 0.45)
    dragon.soul.add_habit("выравнивает стремена к полудню", 0.26)

    print("🐉 Суббота, 3 октября, полдень. Пряжка держит, стремена ещё спорят.")
    print("Короткий круг подождёт ровные пятки.")

    scene("1. После подпруги")
    print(dragon.talk("Подпруга на месте. Выровняй стремена, пожалуйста."))

    scene("2. Левое и правое")
    print(dragon.adjust_stirrup("левое и правое"))

    scene("3. Левое чуть выше")
    print(dragon.adjust_stirrup("левое на одну дырочку выше"))

    scene("4. Ровная посадка")
    print(dragon.talk("Пятки на одной высоте. Можно невысоко над лугом."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после стремян:")
    print(dragon.habits())
    print()
    print("Пятки ровные. Садись, всадник. 🦶")

    save_path = "groktar_saturday_adjust_stirrup.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
