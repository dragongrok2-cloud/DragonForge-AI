"""Вечер понедельника: тихо положить мембрану крыла на седло под тенью после сустава."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и чуть сонный к вечеру",
        backstory="Любит тихие ритуалы у седла перед ночью",
    )
    print(dragon.talk("Положи мембрану крыла на седло"))
    print(dragon.rest_wingmembrane_saddle("под тенью крыла к вечеру понедельника"))


if __name__ == "__main__":
    main()
