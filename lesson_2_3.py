num = int(input('Введите число от 1 до 12'))
calendar = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
if num in calendar[0]:
    print('зима')
elif num in calendar[1]:
    print('весна')
elif num in calendar[2]:
    print('лето')
elif num in calendar[3]:
    print('осень')
else:
    print('Введено некорректное число')


calendar_2 = {'зима': '12, 1, 2', 'весна': '3, 4, 5', 'лето': '6, 7, 8', 'осень': '9, 10, 11'}
if str(num) in calendar_2['зима']:
    print('зима')
elif str(num) in calendar_2['весна']:
    print('весна')
elif str(num) in calendar_2['лето']:
    print('лето')
elif str(num) in calendar_2['осень']:
    print('осень')
else:
    print('Введено некорректное число')
