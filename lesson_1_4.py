number = input("Введите целое положительное число")
i = 0
maximum = number[i]
while i < len(number):
    if number[i] > maximum:
        maximum = number[i]
    i += 1
print(maximum)
