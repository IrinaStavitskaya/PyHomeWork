n = int(input('Введите количество элементов в списке'))
list_1 = []
for i in range(n):
    elem = input('Ведите элемент для списка')
    list_1.append(elem)
list_2 = []

for ind in range(0, n, 2):
    if ind % 2 == 0 and (ind + 1) == n:
        break
    list_1[ind], list_1[ind + 1] = list_1[ind + 1], list_1[ind]
print(list_1)
