"""В воскресенье 11 октября в полдень после глотка в седле: смотрит на горизонт из седла под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_afternoon_gaze_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="полуденный, спокойный, смотрит вдаль из седла",
        backstory="Воскресенье 11 октября, после глотка в седле под тенью в полдень, время взгляда на горизонт",
    )
    print(dragon.sip_saddle("глоток в седле под тенью в полдень"))
    print()
    print(dragon.gaze_saddle("взгляд на горизонт из седла под тенью в полдень"))
    print()
    print(dragon.talk("Посмотри на горизонт"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
