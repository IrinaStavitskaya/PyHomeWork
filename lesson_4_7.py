from math import factorial


def func():
    for el in range(1, n + 1):
        yield factorial(el)


n = int(input('Введите целое число: '))
for elem in func():
    print(elem)
