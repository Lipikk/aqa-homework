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

#Настало время великих стартов: Tesla улетела на гелиоцентрическую орбиту за Марсом, а вам предстоит отправить ракету с питоном на Сатурн. 
#Сгенерируйте строку с обратным предстартовым отсчётом. 

countdown_str = ''
for i in reversed(range(0, 11)):
    countdown_str = countdown_str + str(i) + ', '
print(countdown_str + 'поехали!' )


for messages_count in range(0, 21):
        if messages_count == 0:
        print('У вас нет новых сообщений')
    if messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count == 2:
        print('У вас 2 новых сообщения')
    elif messages_count == 3:
        print('У вас 3 новых сообщения')
    elif messages_count == 4:
        print('У вас 4 новых сообщения')
    else: messages_count >= 5 and messages_count <= 20
    print('У вас', messages_count, 'новых сообщений')