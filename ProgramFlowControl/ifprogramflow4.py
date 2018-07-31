age = int(input("How old are you? "))

if not (age < 18):
    print("Have a good day at work!")
else:
    print("Come back in {} years!".format(18 - age))

pirate = "Jack Sparrow"
letter = input("Enter a character: ")

if letter in pirate:
    print("Give me a an {}, Bob".format(letter))
else:
    print("I don't need that letter")
