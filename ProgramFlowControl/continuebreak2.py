meal = ("rice", "bacon", "pasta", "spam")
nasty_food = ''
for item in meal:
    if item == "bacon":
        nasty_food = item
        break

if nasty_food == "spam":
    print("I need spam more than anything! ")

else:
    print("Ok, I'll have plate of that")
