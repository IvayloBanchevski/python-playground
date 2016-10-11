import random

# Players names
player1 = input("What is player 1 name? ")
player2 = input("What is player 2 name? ")

# Choose dice sides
sides = int(input("Dice sides? "))

# Roll the dice
print("Player 1 rolling the dice...")
roll1 = random.randrange(1, sides)
print(str(roll1))

print("Player 2 rolling the dice...")
roll2 = random.randrange(1, sides)
print(str(roll2))

if (roll1 > roll2):
    print(player1 + " win!")
elif (roll2 > roll1):
    print(player2 + " win!")
else:
    print("Even!")
