list = '9876543210'
iterator_list = iter(list)

for i in range(0, len(list)):
    next_list = next(iterator_list)
    print(next_list)

for i in list:
    print(i)