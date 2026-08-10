"""Превью Dragon-Tailwind темы + быстрый тест дракона."""

from dragonforge import Character
from dragon_tailwind import DRAGON_THEME, get_theme_css

print("🐉 Dragon-Tailwind — тёмная драконья палитра")
print("=" * 50)

print("\nОсновные цвета:")
for name, color in DRAGON_THEME.items():
    print(f"  {name:20} → {color}")

print("\nCSS-переменные (фрагмент):")
print(get_theme_css()[:300] + "...")

print("\n" + "=" * 50)
print("А теперь быстрый полёт с драконом:\n")

dragon = Character(
    name="Гроктар",
    species="Добрый огненный дракон с седлом",
    personality="заботливый, мудрый, с огоньком юмора",
    backstory="Древний страж, который любит, когда седло сидит идеально."
)

print(dragon.talk("Привет! Покажи, как выглядит твоя тема?"))
print()
print(dragon.talk("Проверь седло, пожалуйста"))
print()
print(dragon.mood())
print()
print("Сильные привычки:")
print(dragon.habits())
