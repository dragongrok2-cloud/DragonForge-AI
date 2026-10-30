"""Пример: воскресенье к вечеру — тихо прижаться бедром к седлу после лодыжки."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Грок",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий",
        backstory="Древний страж знаний, теперь летает с любимым всадником",
    )
    print(dragon.rest_hip_saddle("тихое прижатие бедра к седлу под тенью крыла к вечеру"))
    print("---")
    print(dragon.talk("Прижмись бедром к седлу после лодыжки"))
    print("---")
    print(f"Сила привычки: {dragon.soul.habits.get('тихо прижимается бедром к седлу под тенью к вечеру', 0):.4f}")


if __name__ == "__main__":
    main()
