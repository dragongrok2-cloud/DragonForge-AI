"""Пятница, 2 октября: после полёта дракон делится блестящим камушком.

Маленький ритуал коллекции. Седло уже проверено, крылья сложены,
а один камушек переезжает из-под чешуи к всаднику.
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, немного жадный до блеска, но щедрый с всадником",
        backstory="Хранит речные искорки в складке крыла и отдаёт лучшие тем, кто летает рядом",
    )
    print(dragon.talk("Привет! Как прошёл полёт?"))
    print()
    print(dragon.fold_wings())
    print()
    print(dragon.share_pebble(place="седло"))
    print()
    print(dragon.talk("Подари камушек ещё раз, пожалуйста"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
