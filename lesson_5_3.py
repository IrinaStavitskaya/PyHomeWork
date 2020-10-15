import statistics
with open('03_text.txt', 'r') as my_text:
    content = my_text.readlines()
    list_salary = []
    for el in content:
        h = el.split()
        if int(h[1]) < 20000:
            print(h[0])
        list_salary.append(int(h[1]))
    print('Средняя зарплата:', statistics.mean(list_salary))
