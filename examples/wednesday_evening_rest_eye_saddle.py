"""Пример: вечерний ритуал — тихо положить кончик глаза на седло после виска.

Запуск: python examples/wednesday_evening_rest_eye_saddle.py
"""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и тёплый",
        backstory="Любит тихие вечера в седле с всадником"
    )
    print(dragon.talk("Положи глаз на седло"))
    print(dragon.rest_eye_saddle("под тенью крыла к вечеру"))
    print(dragon.habits())


if __name__ == "__main__":
    main()
