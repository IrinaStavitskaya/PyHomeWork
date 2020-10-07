num_1 = int(input('Введите первое число '))
num_2 = int(input('Введите второе число '))
num_3 = int(input('Введите третье число '))


def two_max(x, y, z):
    d = [x, y, z]
    my_min = min(d)
    d.remove(my_min)
    return sum(d)


print(two_max(num_1, num_2, num_3))
