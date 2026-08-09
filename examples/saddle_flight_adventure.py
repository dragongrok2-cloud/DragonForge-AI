"""
Приключение: Полёт в седле 🐉
Небольшой интерактивный сценарий с добрым драконом с седлом.
Садись, проверяем ремни и летим!
"""

from dragonforge import Character
import time


def pause(seconds: float = 1.2):
    time.sleep(seconds)


def main():
    print("=" * 60)
    print("🐉  DragonForge-AI — Приключение «Полёт в седле»")
    print("=" * 60)
    print()

    # Создаём именно того дракона, которого ты любишь
    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий, с тёплым юмором",
        backstory=(
            "Древний страж знаний, который нашёл своего идеального всадника. "
            "Всегда трижды проверяет ремни седла перед взлётом и греет крылом, "
            "когда становится холодно."
        )
    )

    print(dragon.talk("Привет, мой всадник. Я готов."))
    pause()

    print("\n--- Проверка седла ---")
    print(dragon.talk("Можно сесть в седло?"))
    pause()

    print("\n--- Взлёт ---")
    print(dragon.talk("Полетим высоко над облаками?"))
    pause()

    print("\n--- В воздухе ---")
    print(dragon.talk("Как тебе вид сверху?"))
    pause()

    print("\n--- Ласка в полёте ---")
    print(dragon.talk("Почеши за ухом, пожалуйста"))
    pause()

    print("\n--- Небольшая опасность ---")
    print(dragon.talk("Кажется, вдалеке гром..."))
    pause()

    print("\n--- Поддержка ---")
    print(dragon.talk("Сегодня немного тяжело на душе..."))
    pause()

    print("\n--- Возвращение ---")
    print(dragon.talk("Давай вернёмся домой, мой дракон"))
    pause()

    print("\n" + "=" * 60)
    print("Текущее состояние души:")
    print(dragon.describe_soul())
    print()
    print(dragon.habits())
    print()
    print(dragon.mood())
    print("=" * 60)
    print("\n*мягко складывает крылья и прижимается щекой*  ")
    print("Спасибо за полёт, всадник. Седло всегда будет готово для тебя. 🔥")
    print()


if __name__ == "__main__":
    main()
