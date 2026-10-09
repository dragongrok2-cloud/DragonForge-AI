"""После полудня 9 октября: пальцы в полоске солнца, седло не снимаем.

Запуск: python examples/friday_afternoon_curl_fingers.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, держит свет в сгибе пальцев",
        backstory="После полудня 9 октября полоска уже легла на костяшки на Мёде, Шве и Седле",
    )
    print(dragon.shift_stripe("полоска солнца на костяшках после полудня"))
    print()
    print(dragon.curl_fingers("пальцы в полоске солнца после полудня"))
    print()
    print(dragon.talk("Согни пальцы в полоске над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
