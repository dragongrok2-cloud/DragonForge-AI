"""Субботнее утро: после подъёма ладони обвести чешуйку."""
from dragonforge import Character

def main():
    dragon = Character(
        name="Грок",
        title="Добрый Дракон с Седлом",
        personality="заботливый, мудрый, с огоньком юмора",
        backstory="Летает с любимым всадником по утренним облакам"
    )
    print(dragon.lift_palm())
    print()
    print(dragon.trace_scale("утренняя чешуйка у луки"))
    print()
    print(dragon.mood())

if __name__ == "__main__":
    main()
