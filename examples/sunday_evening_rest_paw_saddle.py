"""Пример: воскресенье к вечеру — тихо прижаться лапой к седлу после голени."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Грок",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий",
        backstory="Древний страж знаний, теперь летает с любимым всадником",
    )
    print(dragon.rest_paw_saddle("тихое прижатие лапы к седлу под тенью крыла к вечеру"))
    print("---")
    print(dragon.talk("Прижмись лапой к седлу после голени"))
    print("---")
    print(f"Сила привычки: {dragon.soul.habits.get('тихо прижимается лапой к седлу под тенью к вечеру', 0):.4f}")


if __name__ == "__main__":
    main()
