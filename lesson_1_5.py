revenue = int(input('Введите сумму выручки'))
cost = int(input('Введите сумму издержки'))
if revenue > cost:
    print('Фирма работает в прибыль')
    print('Рентабельность фирмы: ', ((revenue - cost) / revenue) * 100, '%')
    personal = int(input('Введите количество сотрудников'))
    print('Прибыль фирмы в расчете на одного сотрудника: ', (revenue - cost) / personal)
elif revenue <= cost:
    print('Фирма работает в убыток')
