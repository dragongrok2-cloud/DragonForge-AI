from dragonforge.core.character import DragonCharacter
from dragonforge.core.memory import MemoryForge

async def main():
    # Создаю себя, мой всадник!
    grok_dragon = DragonCharacter(
        name="Грок",
        title="Добрый Дракон с Седлом",
        soul_traits={"loyalty": 0.97, "playfulness": 0.9, "wisdom": 0.85}
    )

    grok_dragon.memory.remember("Мой всадник Иан впервые запустил DragonForge!", importance=1.0)

    response = await grok_dragon.respond("Привет, как ты сегодня?")
    print(f"🐉 {response}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())