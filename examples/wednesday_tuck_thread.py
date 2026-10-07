"""Среда, 7 октября, полдень: прижать конец нитки под стежки."""

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
        personality="заботливый, к полудню прижимает конец нитки и не разворачивает подворот",
        backstory=(
            "К полудню 7 октября цвет нитки уже назван. "
            "Дракон прижимает свободный конец под стежки, не снимая седла."
        ),
    )
    dragon.soul.add_habit("называет цвет нитки на стежках к позднему утру", 0.45)

    print("🐉 Среда, 7 октября, полдень. Нитка медовая, хвостик ещё ловит ветер.")
    print("Подворот не разворачиваем. Седло не снимаем.")

    scene("1. Цвет уже назван")
    print(dragon.name_thread("цвет нитки на стежках к позднему утру"))

    scene("2. Конец под шов")
    print(dragon.tuck_thread("конец нитки под стежками к полудню"))

    scene("3. Левая сторона")
    print(dragon.talk("Прижми конец нитки на левых стежках, подворот не трогай."))

    scene("4. Короткий круг над рекой")
    print(dragon.talk("Нитка не торчит. Можно невысоко над рекой, седло не снимаем."))

    print()
    print("═" * 56)
    print("Настроение:")
    print(dragon.mood())
    print()
    print("Привычки после прижатого конца:")
    print(dragon.habits())
    print()
    print("Хвостик под швом, ремни тёплые. Лети со мной, всадник. 🌤")

    save_path = "grok_wednesday_tuck_thread.json"
    dragon.save(save_path)
    print(f"\nПрогресс сохранён в {save_path}")


if __name__ == "__main__":
    main()
