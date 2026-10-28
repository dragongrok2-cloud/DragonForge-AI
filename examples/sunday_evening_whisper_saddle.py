"""В воскресенье 11 октября к вечеру после тихого прижатия мордой к седлу: тихо шепчет седлу под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_whisper_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, тёплый, тихо шепчет седлу",
        backstory="Воскресенье 11 октября, после тихого прижатия мордой к седлу под тенью, время тихо шепнуть",
    )
    print(dragon.nuzzle_saddle("тихое прижатие морды к седлу под тенью к вечеру"))
    print()
    print(dragon.whisper_saddle("тихий шёпот седлу под тенью к вечеру"))
    print()
    print(dragon.talk("Шепни седлу"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
