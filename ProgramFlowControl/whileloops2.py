# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 10
answer = random.randint(1, highest)
guess = 0
# initialize to any number outside of the valid range

print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Bye!")
        break
    if guess < 1 or guess > 10:
        print("Hey! It's only between 1 and 10")
    if guess > answer:
        print("Please guess lower")
    elif guess < answer:
        print("Please guess higher")
    else:
        print("Nice, you guessed it!")
