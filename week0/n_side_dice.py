import random

sides = int(input("Dice sides: "))

diceRoll = random.randrange(1, sides)

print("The dice rolled: " + str(diceRoll))
