print(range(10))
it_list = list(range(10))
print(it_list)

a = list(range(0, 1000, 2))
b = list(range(1, 100, 2))

print(a)
print(b)

my_list = 'abcdefghijklmnoqrstuvwxyz'
print(my_list.index('e'))
print(my_list[4])

small_decimals = range(0, 10)
print(small_decimals)
print(small_decimals.index(3))

c = range(1, 10000, 2)
print(c)

print(c[985])

d = range(7, 1000000, 7)
e = int(input("Enter a number less than 1 million"))
if e in d:
    print("{} is divisible by seven".format(e))

my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))
