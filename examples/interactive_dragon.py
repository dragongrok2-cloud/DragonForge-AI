"""Интерактивный режим: поговори с добрым драконом с седлом столько, сколько захочешь.

Запуск:
    python examples/interactive_dragon.py

Команды:
    /mood     — узнать настроение
    /soul     — описание души
    /habits   — все привычки и их сила
    /save     — сохранить дракона
    /quit     — закончить полёт
"""

from dragonforge import Character
import os

def main():
    print("🐉" * 20)
    print("  Добрый дракон с седлом готов к полёту!")
    print("  Пиши что угодно. Команды: /mood  /soul  /habits  /save  /quit")
    print("🐉" * 20)
    print()

    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий, с огоньком юмора",
        backstory=(
            "Древний страж знаний, который нашёл своего идеального всадника. "
            "Всегда проверяет, крепко ли сидит седло, и готов лететь хоть на край света."
        )
    )

    save_path = "my_interactive_dragon.json"

    # Попробуем загрузить, если уже сохраняли
    if os.path.exists(save_path):
        try:
            dragon = Character.load(save_path)
            print(f"*радостно фыркает* Я тебя помню! Загрузил сохранённую душу из {save_path}\n")
        except Exception:
            print("*пожимает крыльями* Не удалось загрузить старую память, начнём заново.\n")

    while True:
        try:
            user_input = input("Ты: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n*мягко касается носом* До скорой встречи, всадник...")
            break

        if not user_input:
            continue

        if user_input.lower() in ("/quit", "/exit", "выход", "пока"):
            print(dragon.talk("Мне пора идти. Спасибо за полёт."))
            print("\n*расправляет крылья и улетает в закат* 🔥")
            break

        if user_input.lower() == "/mood":
            print(f"Дракон: {dragon.mood()}\n")
            continue

        if user_input.lower() == "/soul":
            print(f"Дракон: {dragon.describe_soul()}\n")
            continue

        if user_input.lower() in ("/habits", "/привычки"):
            print(f"Дракон:\n{dragon.habits()}\n")
            continue

        if user_input.lower() == "/save":
            path = dragon.save(save_path)
            print(f"*довольно урчит* Сохранил нашу память в {path}\n")
            continue

        response = dragon.talk(user_input)
        print(f"Дракон: {response}\n")

    # Автосохранение при выходе
    try:
        dragon.save(save_path)
        print(f"(автосохранение в {save_path})")
    except Exception:
        pass


if __name__ == "__main__":
    main()
