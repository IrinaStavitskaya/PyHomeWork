list_1 = input('Введите список чисел ').split()
list_2 = [i for i in list_1 if list_1.count(i) == 1]
print(list_2)
