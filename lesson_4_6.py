from itertools import count, cycle
n = int(input('Введите целое число: '))
for i in count(n):
    if i > 17:
        break
    else:
        print(i)

z = 0
m = ['a', 'b', 'c']
for el in cycle(''.join(m)):
    if z > 5:
        break
    print(el)
    z += 1
