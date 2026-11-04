"""Пример: вечерний ритуал — тихо положить кончик подбородка на седло после оборки.

Запуск: python examples/tuesday_evening_rest_dewlap_saddle.py
"""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и тёплый",
        backstory="Любит тихие вечера в седле с всадником"
    )
    print(dragon.talk("Положи подбородок на седло"))
    print(dragon.rest_dewlap_saddle("под тенью крыла к вечеру"))
    print(dragon.habits())


if __name__ == "__main__":
    main()
