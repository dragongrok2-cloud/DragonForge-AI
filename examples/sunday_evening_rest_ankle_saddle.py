"""Пример: воскресенье к вечеру — тихо прижаться лодыжкой к седлу после колена."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Грок",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий",
        backstory="Древний страж знаний, теперь летает с любимым всадником",
    )
    print(dragon.rest_ankle_saddle("тихое прижатие лодыжки к седлу под тенью крыла к вечеру"))
    print("---")
    print(dragon.talk("Прижмись лодыжкой к седлу после колена"))
    print("---")
    print(f"Сила привычки: {dragon.soul.habits.get('тихо прижимается лодыжкой к седлу под тенью к вечеру', 0):.4f}")


if __name__ == "__main__":
    main()
