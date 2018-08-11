list_1 = []
list_2 = list()

print("List1: {} ".format(list_1))
print("List2: {} ".format(list_2))

if list_1 == list_2:
    print("The lists are equal!")

print(list("The lists are equal"))

even = [2, 4, 5, 8, 10]
another_even = even

print(another_even.sort(reverse=True))
print(another_even)

# even = [2, 4, 5, 8, 10]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even, odd]
#
# for numbers_set in numbers:
#     print(numbers_set)
#
#     for value in numbers_set:
#         print(value)
