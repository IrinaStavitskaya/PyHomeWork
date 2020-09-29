sec_score = int(input('Введите количесто секунд'))
hours = sec_score // 3600
minute = (sec_score % 3600) // 60
sec = (sec_score % 3600) % 60
print(f"{str(hours).rjust(2, '0')}:{str(minute).rjust(2, '0')}:{str(sec).rjust(2, '0')}")
