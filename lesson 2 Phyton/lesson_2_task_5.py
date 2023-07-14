# Месяц — сезон. Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает название сезона, к которому относится этот месяц.

month = int(input("Введите номер месяца: "))

def month_to_season(month):
    if month in (1, 2, 12):
     print('Зима')
    elif month in (3, 4, 5): 
     print('Весна')
    elif month in (6, 7, 8): 
      print('Лето')
    elif month in (9, 10, 11):
      print('Осень')
    else: print('Некорректный номер месяца')

month_to_season(month)




