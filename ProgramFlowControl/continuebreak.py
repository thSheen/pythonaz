shopping_list = ("bread", "spam", "eggs", "rice", "pasta")

for item in shopping_list:
    if item == "rice":
        print("I'm ignoring " + item)
        # /\ It is optional
        continue

    print("Buy " + item)


shopping_list2 = ("tea", "coffee", "bacon", "milk", "waffles")

for item in shopping_list2:
    if item == "bacon":
        break

    print("Buy " + item)
