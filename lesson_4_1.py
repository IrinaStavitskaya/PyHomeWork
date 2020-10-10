from sys import argv

name, hours, rate, prize = argv

print(f'{int(hours) * int(rate) + int(prize)}')
