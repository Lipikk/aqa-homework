# Месяц — сезон. Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем «Зима»

def month_to_season(month):
    if month in (1, 2, 12): return 'Зима'
    if month in (3, 4, 5): return 'Весна'
    if month in (6, 7, 8): return 'Лето'
    if month in (9, 10, 11): return 'Осень'
    else: return 'Некорректный номер месяца'

print(month_to_season(int(input("Введите номер месяца: "))))

# готово


