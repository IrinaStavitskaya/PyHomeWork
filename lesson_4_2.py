ls_1 = input('Введите список чисел ').split()
ls_2 = [ls_1[i] for i in range(1, len(ls_1)) if ls_1[i] > ls_1[i - 1]]
print(ls_2)
