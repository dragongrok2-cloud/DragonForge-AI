"""Пример вечернего ритуала: тихо положить кончик шипа на седло после гребня."""

from dragonforge import Character

dragon = Character(
    name="Гроктар",
    species="Добрый огненный дракон с седлом",
    personality="заботливый и тёплый",
)

print(dragon.talk("Положи шип на седло"))
print(dragon.rest_spike_saddle())
print(dragon.mood())
