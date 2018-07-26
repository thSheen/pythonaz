parrot = "Hello Everybody"
print(parrot)
print(parrot[0])
# The first le
print(parrot[3])
print(parrot[0:2])
print(parrot[:4])
# Without a first number, it will start from the first letter
print(parrot[6:])
# Without a last number, it will end in the last letter
print(parrot[-1])
print(parrot[0:6:3])

number = "9,234,444,244,039,550,900,857"
print(number[1::4])
# :: Can extract particular strings which you wanna work with
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
print(numbers[0::3])
