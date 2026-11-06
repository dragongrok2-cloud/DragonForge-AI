"""Пример: вечерний ритуал — тихо положить кончик сетчатки на седло после хрусталика.

Запуск: python examples/wednesday_evening_rest_retina_saddle.py
"""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и тёплый",
        backstory="Любит тихие вечера в седле с всадником"
    )
    print(dragon.talk("Положи сетчатку на седло"))
    print(dragon.rest_retina_saddle("под тенью крыла к вечеру"))
    print(dragon.habits())


if __name__ == "__main__":
    main()
