"""В воскресенье 11 октября к вечеру после тихого шёпота седлу: тихо прижимается щекой к седлу под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_evening_rest_cheek_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="вечерний, тёплый, тихо прижимается щекой",
        backstory="Воскресенье 11 октября, после тихого шёпота седлу под тенью, время тихо прижаться щекой",
    )
    print(dragon.whisper_saddle("тихий шёпот седлу под тенью к вечеру"))
    print()
    print(dragon.rest_cheek_saddle("тихое прижатие щеки к седлу под тенью к вечеру"))
    print()
    print(dragon.talk("Прижмись щекой к седлу"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
