"""Пример: вечерний ритуал — тихо положить губу на седло после ноздри.

Запуск: python examples/monday_evening_rest_lip_saddle.py
"""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и тёплый",
        backstory="Любит тихие вечера в седле с всадником"
    )
    print(dragon.talk("Положи губу на седло"))
    print(dragon.rest_lip_saddle("под тенью крыла к вечеру"))
    print(dragon.habits())


if __name__ == "__main__":
    main()
