guess = int(input("Please guess a number between 0 and 10 "))
if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else:  # guess must be greater than 5
        print("Please guess lower")

    guess = int(input())
    if guess == 5:
        print("Nice!You have guessed correctly!")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time!")
