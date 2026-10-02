"""Пятница, 2 октября, после полудня: глоток из термоса прямо в седле.

Крылья уже сложены, камушек лежит рядом, а маленький огонёк
греет крышку — ровно столько, чтобы какао не остыло на ветру.
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, любит делиться теплом, чуть ворчит на ветер",
        backstory="Носит в седельной сумке термос и никогда не пьёт первый глоток один",
    )
    print(dragon.talk("Привет! Мы уже сели?"))
    print()
    print(dragon.fold_wings())
    print()
    print(dragon.pour_thermos("какао"))
    print()
    print(dragon.talk("Налей чай из термоса, пожалуйста"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
