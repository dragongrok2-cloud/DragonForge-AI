"""Пример: сохранение и загрузка дракона."""

from dragonforge import Character

# Создаём дракона
dragon = Character(
    name="Гроктар",
    species="Добрый огненный дракон с седлом",
    personality="заботливый, мудрый, немного дерзкий, с огоньком юмора",
    backstory="Древний страж знаний, который нашёл своего идеального всадника."
)

print("🐉 Создал дракона:")
print(dragon.talk("Привет! Сегодня отличный день для полёта."))
print()

# Сохраняем
path = dragon.save("my_dragon.json")
print(f"💾 Дракон сохранён в {path}")
print()

# Загружаем обратно
loaded = Character.load("my_dragon.json")
print("🔄 Загруженный дракон вспоминает:")
print(loaded.talk("Помнишь, что я говорил про полёт?"))
print()
print("Состояние души после загрузки:")
print(loaded.soul.describe())
