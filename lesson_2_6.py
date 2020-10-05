n = 1
tuple_1 = ()
list_2 = []
while True:
    x = int(input('Если хотите ввести товар, нажмите 1. Если данных для ввода более нет, нажмите 0'))
    if x == 0:
        break
    else:
        name = input('Название: ')
        price = int(input('Цена: '))
        num = int(input('Количество: '))
        unit = input('Единицы измерения: ')
        dates = {'название': name, 'цена': price, 'количество': num, 'ед': unit}
        list_1 = [n, dates]
        tuple_1 = tuple(list_1)
        list_2.append(tuple_1)
        n += 1
print(list_2)
list_3 = {'название': [], 'цена': [], 'количество': [], 'ед': []}
for el in list_2:
    for key in el[1]:
        list_3[key].append(el[1][key])
print(list_3)
