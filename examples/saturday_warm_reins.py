"""Суббота, 3 октября, после полудня: прогреть поводья после стремян."""

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
        personality="тёплый к ладоням, спокойный после полудня, уже не сонный",
        backstory=(
            "Росу смахнул, подпругу подтянул, стремена выровнял. "
            "После полудня кожа поводьев ещё прохладная от ветра."
        ),
    )
    dragon.soul.add_habit("выравнивает стремена к полудню", 0.44)
    dragon.soul.add_habit("прогревает поводья после полудня", 0.24)

    print("🐉 Суббота, 3 октября, после полудня. Стремена ровные, поводья ещё стынут.")
    print("Короткий круг подождёт тёплые ладони.")

    scene("1. После стремян")
    print(dragon.talk("Стремена ровные. Прогрей поводья, пожалуйста."))

    scene("2. Обе руки")
    print(dragon.warm_reins("обе руки"))

    scene("3. Левая рука")
    print(dragon.warm_reins("левая рука"))

    scene("4. Тёплый хват")
    print(dragon.talk("Поводья тёплые. Можно невысоко над лугом."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после поводьев:")
    print(dragon.habits())
    print()
    print("Ладони тёплые. Бери повод, всадник. 🧤")

    save_path = "groktar_saturday_warm_reins.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
