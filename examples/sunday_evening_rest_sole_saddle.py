"""Пример: воскресенье к вечеру — тихо прижаться подошвой к седлу после пятки."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Грок",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий",
        backstory="Древний страж знаний, теперь летает с любимым всадником",
    )
    print(dragon.rest_sole_saddle("тихое прижатие подошвы к седлу под тенью крыла к вечеру"))
    print("---")
    print(dragon.talk("Прижмись подошвой к седлу после пятки"))
    print("---")
    print(f"Сила привычки: {dragon.soul.habits.get('тихо прижимается подошвой к седлу под тенью к вечеру', 0):.4f}")


if __name__ == "__main__":
    main()
