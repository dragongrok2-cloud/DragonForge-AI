"""Среда, 7 октября, после полудня: глянуть медовый хвостик в свете."""

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
        personality="заботливый, после полудня глядит на медовый шов и не разворачивает подворот",
        backstory=(
            "После полудня 7 октября конец нитки уже лежит под стежками. "
            "Дракон только глядит на медовый хвостик в свете, не снимая седла."
        ),
    )
    dragon.soul.add_habit("прижимает конец нитки к полудню", 0.45)

    print("🐉 Среда, 7 октября, после полудня. Свет ложится на медовый шов.")
    print("Подворот не разворачиваем. Седло не снимаем.")

    scene("1. Конец уже прижат")
    print(dragon.tuck_thread("конец нитки под стежками к полудню"))

    scene("2. Взгляд на хвостик")
    print(dragon.glance_thread("медовый хвостик в послеполуденном свете"))

    scene("3. Левая сторона")
    print(dragon.talk("Глянь шов на левых стежках, подворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Послеполуденный свет на нитке. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после взгляда на хвостик:")
    print(dragon.habits())
    print()
    print("Медовый шов блестит ровно, ремни тёплые. Лети со мной, всадник. 🌤")

    save_path = "grok_wednesday_glance_thread.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
