"""Пример: вечерний ритуал — тихо положить кончик рога на седло после хвоста.

Запуск: python examples/monday_evening_rest_horn_saddle.py
"""

from dragonforge import Character

def main():
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый и тёплый",
        backstory="Любит тихие вечера в седле с всадником"
    )
    print(dragon.talk("Положи кончик рога на седло"))
    print(dragon.rest_horn_saddle("под тенью крыла к вечеру"))
    print(dragon.habits())

if __name__ == "__main__":
    main()
