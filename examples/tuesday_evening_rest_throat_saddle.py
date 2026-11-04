"""Пример: вечерний ритуал — тихо положить кончик горла на седло после ваттла.

Запуск: python examples/tuesday_evening_rest_throat_saddle.py
"""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и тёплый",
        backstory="Любит тихие вечера в седле с всадником"
    )
    print(dragon.talk("Положи горло на седло"))
    print(dragon.rest_throat_saddle("под тенью крыла к вечеру"))
    print(dragon.habits())


if __name__ == "__main__":
    main()
