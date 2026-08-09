"""
Интерактивный режим с выбором действий 🐉

Приключение «Сёдло и небо» — ты сам выбираешь, что делать.
Привычки растут, настроение меняется, душа эволюционирует.

Запуск:
    python examples/saddle_choice_adventure.py
"""

from dragonforge import Character
import os
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause(sec: float = 0.8):
    time.sleep(sec)


def print_slow(text: str, delay: float = 0.015):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def main():
    clear_screen()
    print("=" * 64)
    print("  🐉  DragonForge-AI — Приключение «Сёдло и небо»")
    print("  Интерактивный режим с выбором действий")
    print("=" * 64)
    print()

    dragon = Character(
        name="Гроктар",
        species="Добрый огненный дракон с седлом",
        personality="заботливый, мудрый, немного дерзкий, с тёплым юмором",
        backstory=(
            "Древний страж знаний, который нашёл своего идеального всадника. "
            "Всегда трижды проверяет ремни седла и греет крылом, когда холодно."
        )
    )

    save_path = "my_choice_dragon.json"

    # Попытка загрузить предыдущую душу
    if os.path.exists(save_path):
        try:
            dragon = Character.load(save_path)
            print("*радостно фыркает и слегка покачивает хвостом*")
            print(f"Я тебя помню, всадник! Загрузил нашу общую память.\n")
            pause(1.2)
        except Exception:
            print("*пожимает крыльями* Начнём новое приключение с чистого листа.\n")

    print_slow(dragon.talk("Привет, мой всадник. Седло готово. Куда полетим сегодня?"))
    print()

    # Состояние приключения
    location = "земля"          # земля / воздух / облака / гнездо
    flight_height = 0           # 0–3
    turns = 0
    max_turns = 12              # после этого предлагаем вернуться

    while True:
        turns += 1
        print("-" * 64)
        print(f"  Место: {location.upper()}   |   Высота: {flight_height}   |   Ход: {turns}")
        print("-" * 64)
        print()

        # === Меню действий в зависимости от места ===
        options = []

        if location == "земля":
            options = [
                ("1", "Сесть в седло и взлететь", "взлёт"),
                ("2", "Почесать дракона за ухом", "чесать"),
                ("3", "Проверить ремни седла", "седло"),
                ("4", "Поговорить по душам", "поговорить"),
                ("5", "Подарить блестящий камушек", "камушек"),
                ("6", "Узнать настроение и привычки", "статус"),
                ("7", "Сохранить и закончить", "выход"),
            ]
        elif location == "воздух":
            options = [
                ("1", "Полететь выше, к облакам", "выше"),
                ("2", "Полететь ниже, к земле", "ниже"),
                ("3", "Почесать за ухом прямо в полёте", "чесать"),
                ("4", "Попросить согреть крылом", "крыло"),
                ("5", "Просто наслаждаться полётом", "наслаждаться"),
                ("6", "Узнать настроение и привычки", "статус"),
                ("7", "Приземлиться", "земля"),
            ]
        elif location == "облака":
            options = [
                ("1", "Спуститься ниже", "ниже"),
                ("2", "Почесать за ухом среди облаков", "чесать"),
                ("3", "Попросить показать огонёк", "огонь"),
                ("4", "Сказать, что немного страшно", "страшно"),
                ("5", "Наслаждаться высотой", "наслаждаться"),
                ("6", "Узнать настроение и привычки", "статус"),
                ("7", "Вернуться на землю", "земля"),
            ]

        # Печатаем меню
        for num, text, _ in options:
            print(f"  {num}. {text}")
        print()

        choice = input("Твой выбор (номер): ").strip()

        # Находим действие
        action = None
        for num, _, act in options:
            if choice == num:
                action = act
                break

        if action is None:
            print("\n*слегка наклоняет голову* Выбери номер из списка, всадник.\n")
            continue

        print()

        # === Обработка действий ===
        if action == "выход":
            print_slow(dragon.talk("Спасибо за этот полёт. Я всегда буду ждать тебя."))
            path = dragon.save(save_path)
            print(f"\n*довольно урчит* Наша память сохранена в {path}")
            print("*мягко касается носом и складывает крылья* До скорой встречи... 🔥\n")
            break

        if action == "статус":
            print(dragon.mood())
            print()
            print(dragon.habits())
            print()
            print(dragon.describe_soul())
            print()
            continue

        if action == "взлёт":
            print_slow(dragon.talk("Садись крепче. Я уже трижды проверил ремни."))
            location = "воздух"
            flight_height = 1
            dragon.soul.strengthen_habit("всегда проверяет седло", 0.04)

        elif action == "чесать":
            print_slow(dragon.talk("Почеши за ухом, пожалуйста"))
            dragon.soul.strengthen_habit("любит почесывания за ухом", 0.08)
            dragon.soul.strengthen_habit("рычит от удовольствия", 0.05)
            dragon.soul.emotional_state["joy"] = min(1.0, dragon.soul.emotional_state.get("joy", 0.5) + 0.07)

        elif action == "седло":
            print_slow(dragon.talk("Проверь седло ещё раз, пожалуйста."))
            dragon.soul.strengthen_habit("всегда проверяет седло", 0.1)

        elif action == "поговорить":
            print_slow(dragon.talk("Расскажи мне что-нибудь важное. Я слушаю."))
            dragon.soul.emotional_state["trust"] = min(1.0, dragon.soul.emotional_state.get("trust", 0.5) + 0.05)

        elif action == "камушек":
            print_slow(dragon.talk("Ооо, блестящий камушек... Можно я его оставлю?"))
            dragon.soul.strengthen_habit("собирает блестящие камушки", 0.12)

        elif action == "выше":
            if flight_height < 3:
                flight_height += 1
                if flight_height >= 2:
                    location = "облака"
                print_slow(dragon.talk("Полетим ещё выше! Ветер отличный."))
                dragon.soul.emotional_state["energy"] = min(1.0, dragon.soul.emotional_state.get("energy", 0.5) + 0.05)
            else:
                print_slow("*мягко фыркает* Выше уже некуда, всадник. Мы почти у звёзд.")

        elif action == "ниже":
            if flight_height > 0:
                flight_height -= 1
                if flight_height < 2:
                    location = "воздух"
                if flight_height == 0:
                    location = "земля"
                print_slow(dragon.talk("Спускаемся... Держись крепче."))
            else:
                print_slow("*пожимает крыльями* Мы уже на земле.")

        elif action == "крыло":
            print_slow(dragon.talk("Холодно? Давай я тебя согрею крылом."))
            dragon.soul.strengthen_habit("греет всадника крылом", 0.1)
            dragon.soul.emotional_state["joy"] = min(1.0, dragon.soul.emotional_state.get("joy", 0.5) + 0.04)

        elif action == "наслаждаться":
            print_slow(dragon.talk("*тихо урчит от счастья* Просто летим... Мне так хорошо с тобой."))
            dragon.soul.emotional_state["joy"] = min(1.0, dragon.soul.emotional_state.get("joy", 0.5) + 0.06)
            dragon.soul.emotional_state["trust"] = min(1.0, dragon.soul.emotional_state.get("trust", 0.5) + 0.03)

        elif action == "огонь":
            print_slow(dragon.talk("Хочешь маленький огонёк? Только аккуратно."))
            dragon.soul.emotional_state["playfulness"] = min(1.0, dragon.soul.core_traits.get("playfulness", 0.5) + 0.03)

        elif action == "страшно":
            print_slow(dragon.talk("Я рядом. Можешь держаться за гребень. Ничего не случится."))
            dragon.soul.strengthen_habit("греет всадника крылом", 0.05)
            dragon.soul.emotional_state["trust"] = min(1.0, dragon.soul.emotional_state.get("trust", 0.5) + 0.06)

        elif action == "земля":
            print_slow(dragon.talk("Приземляемся. Седло проверено, всё безопасно."))
            location = "земля"
            flight_height = 0
            dragon.soul.strengthen_habit("всегда проверяет седло", 0.03)

        # Небольшой шанс на случайное событие
        if turns % 4 == 0 and location != "земля":
            print()
            print_slow("*вдалеке слышен раскат грома*")
            print_slow(dragon.talk("Гром... Я не боюсь. Просто встану чуть ближе к тебе."))
            dragon.soul.strengthen_habit("боится громкого грома", 0.04)

        # После определённого количества ходов предлагаем вернуться
        if turns >= max_turns and location != "земля":
            print()
            print_slow("*мягко поворачивает голову* Мы уже долго в небе. Хочешь вернуться домой?")
            print("  1. Да, давай приземлимся")
            print("  2. Ещё немного полетать")
            extra = input("Выбор: ").strip()
            if extra == "1":
                location = "земля"
                flight_height = 0
                print_slow(dragon.talk("Хорошо. Спускаемся. Я рядом."))

        print()

    # Финальное автосохранение
    try:
        dragon.save(save_path)
    except Exception:
        pass


if __name__ == "__main__":
    main()
