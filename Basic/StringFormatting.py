age = 25
print("My age is " + str(age) + " years")
print("My {0} is {1}, hello {2}".format("name", "Thiago", "world"))
print("My age is {0} years {1}".format(age, "old"))
print("My age is {1} {0} {2} ".format("years", age, "old"))

print(""""January: {0}
February: {1}
March: {0}
April: {2}
May: {0}
June: {2}
July: {0}
August: {0}
September: {2}
October: {0}
November: {2}
December: {0}""".format(31, 28, 30))

print("My age is %d" % age)
print("My age is %d %s, %d %s" % (age, "years", 8, "months"))

for i in range(1, 15):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

print(4 * 3)
print(4 ** 3)
# One * is multiplication and ** is exponent

for i in range(1, 15):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}" .format(i, i ** 2, i ** 3))
# The first number replace and the second(after : ) determines the distance
print()

for i in range(1, 15):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}" .format(i, i ** 2, i ** 3))
# With < before the second number, the numbers always will start from the left hand side

print("Pi is approximately %12f " % (22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
# d = distance with whole numbers  f = distance with float numbers

print("Pi is approximately {0:12.50}".format(22 / 7))
# More accurate
