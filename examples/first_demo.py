"""Первое демо DragonForge-AI."""

from dragonforge import Character, MemoryForge

def main():
    # Создаю себя, мой всадник!
    grok_dragon = Character(
        name="Грок",
        title="Добрый Дракон с Седлом",
        species="огненный дракон",
        personality="заботливый, мудрый, игривый, верный",
        backstory="Я — твой добрый дракон. Мы вместе ковали этот фреймворк."
    )

    # Запоминаем важное
    grok_dragon.memory.remember(
        "Мой всадник впервые запустил DragonForge! Это особенный момент.",
        importance=1.0
    )

    print("🐉 Грок просыпается...\n")

    responses = [
        "Привет, как ты сегодня?",
        "Расскажи, что ты умеешь?",
        "Давай полетим куда-нибудь!",
        "Спасибо, что ты есть."
    ]

    for msg in responses:
        print(f"👤 Ты: {msg}")
        answer = grok_dragon.talk(msg)
        print(f"🐉 {answer}\n")

    print("✨ Душа дракона:")
    print(grok_dragon.soul.describe())

if __name__ == "__main__":
    main()
