#калькулятор

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number_1 in numbers:
    for number_2 in numbers:
        print(number_1, '*', number_2, '=', number_1 * number_2)


# этажи

print('Это первый этаж.')
# Первый этаж построен, начинайте строить со второго
for i in range(2, 11):
    # Здесь вместо многоточий
    # вставьте номер текущего этажа,
    # вычислите и вставьте номер предыдущего этажа.
    print('А это', i , 'этаж, он на один выше, чем этаж', i-1)

# месяцы наоборот

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

for i in reversed(months):
    print(i)
