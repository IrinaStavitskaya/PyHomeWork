with open('04_text.txt', 'r', encoding='utf-8') as my_text:
    content = my_text.readlines()
    new_list = []
    for line in content:
        list_line = line.split()
        if list_line[0] == 'One':
            list_line[0] = 'Один'
        elif list_line[0] == 'Two':
            list_line[0] = 'Два'
        elif list_line[0] == 'Three':
            list_line[0] = 'Три'
        elif list_line[0] == 'Four':
            list_line[0] = 'Четыре'
        new_list.append(' '.join(list_line))
with open('04_1_text.txt', 'w', encoding='utf-8') as my_text2:
    my_text2.writelines([i + '\n' for i in new_list])
