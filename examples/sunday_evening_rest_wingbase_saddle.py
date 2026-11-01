"""Вечер воскресенья: тихо положить основание крыла на седло под тенью после крыла."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и чуть сонный к вечеру",
        backstory="Любит тихие ритуалы у седла перед ночью",
    )
    print(dragon.talk("Положи основание крыла на седло"))
    print(dragon.rest_wingbase_saddle("под тенью крыла к вечеру воскресенья"))


if __name__ == "__main__":
    main()
