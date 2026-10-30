"""Пример: вечерний ритуал — тихо положить кончик когтя на седло после кончика хвоста."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и чуть сонный к вечеру",
        backstory="Любит тихие ритуалы в седле под крылом"
    )

    print("=== Вечер в седле: кончик когтя ===\n")
    print(dragon.talk("Положи кончик когтя на седло"))
    print()
    print(dragon.rest_claw_saddle("после тихого кончика хвоста, под тенью крыла"))
    print()
    print("Привычка:", dragon.soul.get_habit_strength("тихо кладёт кончик когтя на седло под тенью к вечеру"))


if __name__ == "__main__":
    main()
