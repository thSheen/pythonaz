greeting = "Hello"
Greeting = "World"
_NAME = "Thiago"
Thiago34 = "What"
t123 = "Wonderful"

print(greeting + ' ' + _NAME)
print(Greeting + ' ' + Thiago34 + ' ' + t123)

a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
# // to whole numbers, it's important use it to prevent future errors

# Example :
for i in range(1, a//b):
    print(i)

# It doesn't work if just use one /

# Wrong :
print(a + b / 3 -4 * 12)
# Right :
print((((a + b)/3)-4)*12)