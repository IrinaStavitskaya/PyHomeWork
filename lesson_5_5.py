with open('05_text.txt', 'w+') as my_text:
    list_num = [i for i in input().split()]
    list_num2 = [el + ' ' for el in list_num]
    my_text.writelines(list_num2)
    my_text.seek(0)
    print(sum([int(i) for i in (my_text.read()).strip().split()]))
