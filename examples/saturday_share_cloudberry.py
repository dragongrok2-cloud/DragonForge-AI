"""Суббота, 3 октября, после полудня: ягода из седельной сумки после поводьев."""

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
        personality="щедрый к ладоням, спокойный после полудня, любит сладкий ветер",
        backstory=(
            "Росу смахнул, подпругу подтянул, стремена выровнял, поводья прогрел. "
            "В седельной сумке ещё тёплая облачная ягода."
        ),
    )
    dragon.soul.add_habit("прогревает поводья после полудня", 0.44)
    dragon.soul.add_habit("делится облачной ягодой после поводьев", 0.23)

    print("🐉 Суббота, 3 октября, после полудня. Поводья тёплые, сумка чуть пахнет мёдом.")
    print("Короткий круг подождёт сладкий глоток.")

    scene("1. После поводьев")
    print(dragon.talk("Поводья тёплые. Поделись ягодой, пожалуйста."))

    scene("2. Облачная ягода")
    print(dragon.share_cloudberry("облачная ягода"))

    scene("3. Морошка")
    print(dragon.share_cloudberry("морошка"))

    scene("4. Сладкий ветер")
    print(dragon.talk("Ягода сладкая. Можно невысоко над лугом."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после ягоды:")
    print(dragon.habits())
    print()
    print("Ладонь сладкая. Бери повод, всадник. 🫐")

    save_path = "groktar_saturday_share_cloudberry.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
