with open('02_text.txt', 'r') as my_text:
    content = my_text.readlines()
    print(f'Количество строк: {len(content)}')
    n = 1
    for el in content:
        h = el.split()
        print(f'Длина строки {n}: {len(h)}')
        n += 1
