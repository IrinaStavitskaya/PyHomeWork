import json
with open('07_text.txt', 'r', encoding='utf-8') as my_text:
    x = my_text.readlines()
    m = [el.split() for el in x]
    ave_profit = 0
    n = 1
    my_list = []
    for i in m:
        profit = int(i[2]) - int(i[3])
        if profit > 0:
            ave_profit = (ave_profit + profit) / n
            n += 1
        else:
            profit = 'no profit'
        print(f'Profit {i[0]}: {profit}')
    print(f'Average profit: {ave_profit}')
    dict_1 = {i[0]: int(i[2]) - int(i[3]) for i in m if int(i[2]) - int(i[3]) > 0}
    dict_2 = {i[0]: 'no profit' for i in m if int(i[2]) - int(i[3]) <= 0}
    dict_3 = {'average profit': ave_profit}
    my_list.append(dict_1)
    my_list.append(dict_2)
    my_list.append(dict_3)
    print(my_list)
with open('lesson_5_7.json', 'w') as my_file:
    json.dump(my_list, my_file)
