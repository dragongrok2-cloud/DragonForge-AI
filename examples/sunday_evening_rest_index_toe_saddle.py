"""Вечер воскресенья: тихо прижаться указательным пальцем стопы к седлу под тенью крыла после безымянного."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и чуть сонный к вечеру",
        backstory="Любит тихие ритуалы у седла перед ночью",
    )
    print(dragon.talk("Прижмись указательным пальцем стопы к седлу"))
    print(dragon.rest_index_toe_saddle("под тенью крыла к вечеру воскресенья"))


if __name__ == "__main__":
    main()
