"""В субботу 10 октября после полудня: ладонью гладит луку после утреннего нюзла, седло не снимаем.

Запуск: python examples/saturday_afternoon_stroke_pommel.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, гладит луку ладонью",
        backstory="Суббота 10 октября, после утреннего нюзла и выдоха, лука ждёт ладони",
    )
    print(dragon.nuzzle_pommel("луку утром после выдоха"))
    print()
    print(dragon.stroke_pommel("луку после полудня после нюзла"))
    print()
    print(dragon.talk("Погладь луку над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
