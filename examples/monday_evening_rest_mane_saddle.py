"""Пример: вечерний ритуал — тихо положить кончик гривы на седло после усика.

Запуск: python examples/monday_evening_rest_mane_saddle.py
"""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и тёплый",
        backstory="Любит тихие вечера в седле с всадником"
    )
    print(dragon.talk("Положи гриву на седло"))
    print(dragon.rest_mane_saddle("под тенью крыла к вечеру"))
    print(dragon.habits())


if __name__ == "__main__":
    main()
