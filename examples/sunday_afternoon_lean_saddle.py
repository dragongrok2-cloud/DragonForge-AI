"""В воскресенье 11 октября после тихого напевания в седле: опирается спиной на луку в седле под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_afternoon_lean_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="полуденный, спокойный, опирается в седле",
        backstory="Воскресенье 11 октября, после тихого напевания в седле под тенью, время опереться спиной на луку",
    )
    print(dragon.hum_saddle("тихое напевание в седле под тенью в полдень"))
    print()
    print(dragon.lean_saddle("опирание спиной на луку в седле под тенью после полудня"))
    print()
    print(dragon.talk("Опрись в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
