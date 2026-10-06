"""Вторник, 6 октября, после полудня: край крыла после тени."""

from dragonforge import Character


def scene(title: str) -> None:
    print()
    print("─" * 56)
    print(title)
    print("─" * 56)


def main() -> None:
    dragon = Character(
        name="Грок",
        title="Добрый дракон с седлом",
        personality="заботливый, тихий после полудня, не снимает седло без просьбы",
        backstory=(
            "В полдень 6 октября край крыла держал тень над лукой. "
            "Солнце уже не жжёт, и дракон чуть опускает край, чтобы в седле повеяло."
        ),
    )
    dragon.soul.add_habit("держит тень над лукой в полдень", 0.4)

    print("🐉 Вторник, 6 октября, после полудня. Тень сделала своё.")
    print("Крыло не убираем в складку. Только опускаем край.")

    scene("1. Тень ещё над лукой")
    print(dragon.shade_pommel("тень крыла над лукой в полдень"))

    scene("2. Край чуть ниже")
    print(dragon.ease_wing("край крыла после полуденной тени"))

    scene("3. Стремя тоже дышит")
    print(dragon.talk("Опусти край крыла над стременем после тени."))

    scene("4. Короткий прохладный круг")
    print(dragon.talk("Лука уже не горячая. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после опущенного края:")
    print(dragon.habits())
    print()
    print("Ветер под крылом, ремни на месте. Лети со мной, всадник. 🌤")

    save_path = "grok_tuesday_ease_wing.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
