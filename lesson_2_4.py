str_1 = input('Введите несколько слов через пробел').split()
num_str = 1
for el in str_1:
    print(f'{num_str} : {el[:10]}')
    num_str += 1
