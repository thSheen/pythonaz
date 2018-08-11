number = "9, 223, 372, 036, 854, 775, 807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char
newNumber = int(cleanedNumber)
print("The new number is {}".format(newNumber))

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals letters in the quote above.
for char in quote:
    if char in "QAZWSXEDCRFVTGBYHNUJMIKOLPÇ":
        print(char)
