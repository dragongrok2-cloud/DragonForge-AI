"""К середине утра 9 октября: бусинка росы со стекла, седло не снимаем.

Запуск: python examples/friday_midmorning_blot_bead.py
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый дракон с седлом",
        personality="тихий, тёплый, не вытаскивает фонарик",
        backstory="К середине утра 9 октября ладони уже согрели стекло на Мёде, Шве и Седле",
    )
    print(dragon.cup_glow("ладони о стекло фонарика под краем попоны утром"))
    print()
    print(dragon.blot_bead("бусинка росы со стекла фонарика к середине утра"))
    print()
    print(dragon.talk("Промокни бусинку росы со стекла над рекой"))
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
