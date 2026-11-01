"""Вечер воскресенья: тихо положить крыло на седло под тенью после бока."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и чуть сонный к вечеру",
        backstory="Любит тихие ритуалы у седла перед ночью",
    )
    print(dragon.talk("Положи крыло на седло"))
    print(dragon.rest_wing_saddle("под тенью крыла к вечеру воскресенья"))


if __name__ == "__main__":
    main()
