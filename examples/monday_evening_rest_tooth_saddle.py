"""Пример: вечерний ритуал — тихо положить кончик зуба на седло после клыка.

Запуск: python examples/monday_evening_rest_tooth_saddle.py
"""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и тёплый",
        backstory="Любит тихие вечера в седле с всадником"
    )
    print(dragon.talk("Положи зуб на седло"))
    print(dragon.rest_tooth_saddle("под тенью крыла к вечеру"))
    print(dragon.habits())


if __name__ == "__main__":
    main()
