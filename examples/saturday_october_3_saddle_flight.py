"""Субботний полёт 3 октября: роса на седле перед выходными."""

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
        personality="заботливый, чуть сонный после пятницы, уже готовый к выходным",
        backstory=(
            "После ночного разворота к гнезду встречает субботу росой на луке седла. "
            "Сначала смахивает капли, потом зовёт всадника в невысокий утренний круг."
        ),
    )
    dragon.soul.add_habit("любит субботние рассветы", 0.55)
    dragon.soul.add_habit("смахивает утреннюю росу с седла", 0.3)

    print("🐉 Суббота, 3 октября. Гнездо ещё тёплое, седло в росе.")
    print("Крыло не торопится. Выходные можно начать тихо.")

    scene("1. Пробуждение у гнезда")
    print(dragon.talk("Доброе утро. На седле роса — смахнёшь, пока я застёгиваю сумки?"))
    dragon.soul.strengthen_habit("любит субботние рассветы", 0.04)

    scene("2. Ритуал росы")
    print(dragon.brush_dew("лука седла"))

    scene("3. Стремена тоже мокрые")
    print(dragon.brush_dew("стремена"))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Роса смахнута. Можно невысоко над рекой, пока солнце не поднялось."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после росы:")
    print(dragon.habits())
    print()
    print("Седло сухое, ремни не скользят. Лети со мной, всадник. 💧")

    save_path = "groktar_saturday_october_3_saddle_flight.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
