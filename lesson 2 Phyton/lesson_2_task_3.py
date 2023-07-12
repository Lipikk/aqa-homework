# Високосный год: создайте функцию is_year_leap, принимающую 1 аргумент — год (число) — и возвращающую True, если год високосный, и False — иначе


def is_year_leap(year):
    year1 = ''
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
      print("год + print(year1): True")
    else: 
      print("год + print(year1): False")

is_year_leap(int(input('Введите год: ')))

    
