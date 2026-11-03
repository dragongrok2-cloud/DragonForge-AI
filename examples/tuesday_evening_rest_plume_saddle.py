"""Пример вечернего ритуала: тихо положить кончик пера на седло после хохлика."""

from dragonforge import Character

dragon = Character(
    name="Гроктар",
    species="Добрый огненный дракон с седлом",
    personality="заботливый и тёплый",
)

print(dragon.talk("Положи перо на седло"))
print(dragon.rest_plume_saddle())
print(dragon.mood())
