"""Вечер воскресенья: тихо прижаться спиной к седлу под тенью крыла после живота."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и чуть сонный к вечеру",
        backstory="Любит тихие ритуалы у седла перед ночью",
    )
    print(dragon.talk("Прижмись спиной к седлу"))
    print(dragon.rest_back_saddle("под тенью крыла к вечеру воскресенья"))


if __name__ == "__main__":
    main()
