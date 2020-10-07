num_1 = float(input('Введите действительное положительное число '))
num_2 = int(input('Введите целое отрицательное число '))


def my_func1(x, y):
    return x ** y


print(my_func1(num_1, num_2))


def my_func2(x, y):
    m = 1
    for i in range(abs(y)):
        m *= (1 / x)
    return m


print(my_func2(num_1, num_2))
