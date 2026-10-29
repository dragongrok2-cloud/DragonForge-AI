"""В воскресенье 11 октября к вечеру после тихого прижатия шеей: тихо прижимается плечом к седлу под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_rest_shoulder_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, тёплый, тихо прижимается плечом",
        backstory="Воскресенье 11 октября, после тихого прижатия шеей под тенью, время тихо прижаться плечом",
    )
    print(dragon.rest_neck_saddle("тихое прижатие шеи к седлу под тенью к вечеру"))
    print()
    print(dragon.rest_shoulder_saddle("тихое прижатие плеча к седлу под тенью к вечеру"))
    print()
    print(dragon.talk("Прижмись плечом к седлу"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
