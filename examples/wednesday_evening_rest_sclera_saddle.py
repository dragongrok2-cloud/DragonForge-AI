"""Пример: вечерний ритуал — тихо положить кончик склеры на седло после радужки.

Запуск: python examples/wednesday_evening_rest_sclera_saddle.py
"""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и тёплый",
        backstory="Любит тихие вечера в седле с всадником"
    )
    print(dragon.talk("Положи склеру на седло"))
    print(dragon.rest_sclera_saddle("под тенью крыла к вечеру"))
    print(dragon.habits())


if __name__ == "__main__":
    main()
