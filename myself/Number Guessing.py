import random
import math

# Taking Inputs
lower = int(input("Enter lower bound:\t"))
upper = int(input("Enter upper bound:\t"))

# generating random number between the lower and upper
x = random.randint(lower, upper)
print("you've only 10 chances to guess the integer!\n")

# Intializing the number of guesses.
count = 0

# for calculation of minimum number of guesses depends upon range
while count <= 10:
    count += 1

    # Taking guessing number as input
    guess = int(input("Guess a number:\t"))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in", count,"try")
        break
    elif x > guess:
        print("You guessed too small !")
    elif x < guess:
        print("You guessed too high !")

# If guessing is more than required guesses, shows this output
if count > 10 :
    print("The number is", x)
    print("\nBetter Luck Next Time !")