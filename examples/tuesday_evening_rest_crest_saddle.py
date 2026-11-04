"""Пример вечернего ритуала: тихо положить кончик гребня на седло после пера."""

from dragonforge import Character

dragon = Character(
    name="Гроктар",
    species="Добрый огненный дракон с седлом",
    personality="заботливый и тёплый",
)

print(dragon.talk("Положи гребень на седло"))
print(dragon.rest_crest_saddle())
print(dragon.mood())
