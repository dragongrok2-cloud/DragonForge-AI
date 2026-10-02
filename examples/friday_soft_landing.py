"""Пятница, 2 октября — мягкая посадка перед выходными.

Утренний полёт уже был. К полудню дракон сам предлагает спираль вниз:
седло на месте, крылья сложены, выходные можно встретить на земле.
"""

from dragonforge import Character


def main() -> None:
    dragon = Character(
        name="Грок",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий",
        backstory="Утром 2 октября уже летал с всадником, теперь сажает его к выходным",
    )
    dragon.memory.remember(
        "Пятница 2 октября: утренний полёт в седле уже состоялся.",
        importance=0.8,
    )

    print(dragon.talk("Пора садиться, выходные близко"))
    print()
    print(dragon.soft_landing())
    print()
    dragon.soul.emotional_state["energy"] = 0.32
    print(dragon.soft_landing())
    print()
    print(dragon.habits())


if __name__ == "__main__":
    main()
