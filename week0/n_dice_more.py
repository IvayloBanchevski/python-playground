import random

# Let user choose dice sides
diceSides = int(input("Dice sides: "))

resultSum = 0

# Roll the dice 3 times
for i in range(0, 3):
    if (diceSides != 1):
        print("Roll " + str(i+1))
        rolled = random.randrange(1, diceSides)
        print(str(rolled))
        resultSum += rolled

# Print the sum.
print("Sum: " + str(resultSum))
