"""К вечеру 9 октября: сгиб полоски солнца, седло не снимаем.

Запуск: python examples/friday_evening_ease_fold.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, держит тепло сгиба на костяшках",
        backstory="К вечеру 9 октября пальцы уже согнуты в полоске на Мёде, Шве и Седле",
    )
    print(dragon.curl_fingers("пальцы в полоске солнца после полудня"))
    print()
    print(dragon.ease_fold("сгиб полоски солнца к вечеру"))
    print()
    print(dragon.talk("Разжми сгиб над рекой к вечеру"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
