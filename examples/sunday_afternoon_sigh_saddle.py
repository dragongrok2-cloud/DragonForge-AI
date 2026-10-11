"""В воскресенье 11 октября после опирания спиной на луку в седле: тихо вздыхает в седле под тенью крыла, седло не снимаем.

Запуск: python examples/sunday_afternoon_sigh_saddle.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="полуденный, спокойный, вздыхает в седле",
        backstory="Воскресенье 11 октября, после опирания спиной на луку в седле под тенью, время тихо вздохнуть",
    )
    print(dragon.lean_saddle("опирание спиной на луку в седле под тенью после полудня"))
    print()
    print(dragon.sigh_saddle("тихий вздох в седле под тенью после полудня"))
    print()
    print(dragon.talk("Вздохни в седле"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
