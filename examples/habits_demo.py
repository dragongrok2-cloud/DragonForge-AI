"""Демонстрация системы привычек дракона."""

from dragonforge import Character

dragon = Character(
    name="Гроктар",
    species="Добрый огненный дракон с седлом",
    personality="заботливый, мудрый, с огоньком юмора",
    backstory="Древний страж, который любит своего всадника и свои привычки."
)

print("🐉 Начальные привычки:")
print(dragon.habits())
print()

print("=" * 50)
print("Разговариваем и укрепляем привычки...\n")

# Укрепляем привычки через разговор
print(dragon.talk("Можно сесть в седло?"))
print()
print(dragon.talk("Почеши за ухом, пожалуйста"))
print()
print(dragon.talk("Почеши ещё раз, так приятно"))
print()
print(dragon.talk("Мне немного холодно"))
print()
print(dragon.talk("Смотри, какой блестящий камушек!"))
print()

print("=" * 50)
print("\n🐉 Привычки после общения:")
print(dragon.habits())
print()
print("Описание души:")
print(dragon.describe_soul())
