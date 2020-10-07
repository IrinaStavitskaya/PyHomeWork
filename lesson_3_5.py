sum_num = 0
while True:
    d = [i for i in input('Вводите числа через пробел. \nДля выхода из программы нажмите q \n').split()]
    if d[len(d) - 1] == 'q':
        d.remove('q')
        d_2 = [int(i) for i in d]
        sum_num += sum(d_2)
        print(sum_num)
        break
    d_2 = [int(i) for i in d]
    sum_num += sum(d_2)
    print(sum_num)
