"""В воскресенье 11 октября после взгляда на горизонт из седла: тихо напевает мягкую мелодию в седле под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_afternoon_hum_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="полуденный, спокойный, напевает в седле",
        backstory="Воскресенье 11 октября, после взгляда на горизонт из седла под тенью, время тихого напевания",
    )
    print(dragon.gaze_saddle("взгляд на горизонт из седла под тенью в полдень"))
    print()
    print(dragon.hum_saddle("тихое напевание в седле под тенью в полдень"))
    print()
    print(dragon.talk("Напой в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
