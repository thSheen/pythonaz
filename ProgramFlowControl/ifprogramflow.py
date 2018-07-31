#
# name = input("Please enter your name")
# age = int(input("How old are you, {}?".format(name)))
#
#
# if age >= 18:
#     print("You are old enough to drive")
#     print("Please, if you drive, don't be drunk!")
# else:
#     print("Please come back in {} years".format(18 - age))

guess = int(input("Please guess a number between 0 and 10 "))

if guess < 5:
    print("Please, guess higher")
    guess = int(input())
    if guess == 5:
        print("Well done!")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > 5:
    print("Please, guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done!")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time!")
