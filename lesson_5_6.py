import re
with open('06_text.txt', 'r', encoding='utf-8') as my_text:
    list_1 = my_text.readlines()
    m = []
    my_dict = {}
    for el in list_1:
        nums = [int(i) for i in re.findall(r'\d+', el)]
        m.append(sum(nums))
    list_2 = [i.split() for i in list_1]
    list_3 = [i[0] for i in list_2]
    my_dict = dict(zip(list_3, m))
    print(my_dict)
