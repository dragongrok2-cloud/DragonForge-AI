"""Пример: вечерний ритуал — тихо положить кончик стекловидного тела на седло после фовеи.

Запуск: python examples/wednesday_evening_rest_vitreous_saddle.py
"""

from dragonforge import Character


def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и тёплый",
        backstory="Любит тихие вечера в седле с всадником"
    )
    print(dragon.talk("Положи стекловидное тело на седло"))
    print(dragon.rest_vitreous_saddle("под тенью крыла к вечеру"))
    print(dragon.habits())


if __name__ == "__main__":
    main()
