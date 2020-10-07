x = int(input('Введите первое число'))
y = int(input('Введите второе число'))


def div(x_1, y_1):
    try:
        return x_1 / y_1
    except ZeroDivisionError:
        return 0.0


print(div(x, y))
