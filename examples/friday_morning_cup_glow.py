"""Утром 9 октября: ладони о стекло фонарика под краем, седло не снимаем.

Запуск: python examples/friday_morning_cup_glow.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, не вытаскивает фонарик",
        backstory="Утром 9 октября фонарик уже лежит под разглаженным краем на Мёде, Шве и Седле",
    )
    print(dragon.tuck_lantern("фонарик под разглаженный край попоны к вечеру"))
    print()
    print(dragon.cup_glow("ладони о стекло фонарика под краем попоны утром"))
    print()
    print(dragon.talk("Согрей ладони о стекло фонарика над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
