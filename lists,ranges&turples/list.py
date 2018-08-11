# ipAddress = input("Please enter your IP ")
# print(ipAddress.count("."))

parrot_link = ["non pinin'", "no more", "a stiff", "bereft of life"]

parrot_link.append("A Norwegian blue")

for state in parrot_link:
    print("The parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers_in_order = sorted(numbers)

print(numbers_in_order)

if numbers == numbers_in_order:
    print("The list are equal")
else:
    print("The list are not equal")

if numbers_in_order == sorted(numbers):
    print("The list are equal")
else:
    print("The list are not equal")