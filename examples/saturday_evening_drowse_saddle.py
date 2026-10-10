"""В субботу 10 октября к ночи: после уюта в седле мягко дремлет, крылья чуть сильнее складывает, седло не снимаем.

Запуск: python examples/saturday_evening_drowse_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="уютный, тихий, дремлет в седле к ночи",
        backstory="Суббота 10 октября, после уюта в седле, ночь ждёт мягкого дремания",
    )
    print(dragon.nestle_saddle("седло к вечеру после луки"))
    print()
    print(dragon.drowse_saddle("седло к ночи после уюта"))
    print()
    print(dragon.talk("Дремли в седле под звёздами"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
