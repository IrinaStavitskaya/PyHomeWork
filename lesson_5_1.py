with open('01_text.txt', 'w') as my_text:
    a = 0
    while a != '':
        a = input('Введите текст: ')
        my_text.write(a + '\n')
