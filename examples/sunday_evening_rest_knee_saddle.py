"""Пример: воскресенье к вечеру — тихо прижаться коленом к седлу после когтя."""

from dragonforge import Character


def main():
    dragon = Character(
        name="Грок",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий",
        backstory="Древний страж знаний, теперь летает с любимым всадником",
    )
    print(dragon.rest_knee_saddle("тихое прижатие колена к седлу под тенью крыла к вечеру"))
    print("---")
    print(dragon.talk("Прижмись коленом к седлу после когтя"))
    print("---")
    print(f"Сила привычки: {dragon.soul.habits.get('тихо прижимается коленом к седлу под тенью к вечеру', 0):.4f}")


if __name__ == "__main__":
    main()
