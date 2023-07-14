# Високосный год: создайте функцию is_year_leap, принимающую 1 аргумент — год (число) — и возвращающую True, если год високосный, 
# и False — иначе

def is_year_leap(year = int(input('Введите год: '))):   
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
      print("год", year, "True")
    else: 
      print("год", year, "False")

is_year_leap()

#готово
