# Contrast between "for loops" and "while loops"
# for i in range(10):
#     print("i is now {}".format(i))

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

available_exists = ["east", "north east", "south"]

chosen_exit = ""
while chosen_exit not in available_exists:
    chosen_exit = input("Please choose a direction ")
    if chosen_exit == "quit":
        print("Game Over!")
        break
else:
    print("Nice, you got out of there!")
