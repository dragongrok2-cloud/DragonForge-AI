"""Вечер понедельника: тихо положить ребро крыла на седло под тенью после сложения."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и чуть сонный к вечеру",
        backstory="Любит тихие ритуалы у седла перед ночью",
    )
    print(dragon.talk("Положи ребро крыла на седло"))
    print(dragon.rest_wingrib_saddle("под тенью крыла к вечеру понедельника"))


if __name__ == "__main__":
    main()
