"""Вечер понедельника: тихо положить хребет на седло под тенью после ребра."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и чуть сонный к вечеру",
        backstory="Любит тихие ритуалы у седла перед ночью",
    )
    print(dragon.talk("Положи хребет на седло"))
    print(dragon.rest_spine_saddle("под тенью крыла к вечеру понедельника"))


if __name__ == "__main__":
    main()
