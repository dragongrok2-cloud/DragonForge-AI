"""Пример вечернего ритуала: тихо положить кончик хохлика на седло."""

from dragonforge import Character

dragon = Character(
    name="Гроктар",
    species="Добрый огненный дракон с седлом",
    personality="заботливый и тёплый",
)

print(dragon.talk("Положи хохлик на седло"))
print(dragon.rest_tuft_saddle())
print(dragon.mood())
