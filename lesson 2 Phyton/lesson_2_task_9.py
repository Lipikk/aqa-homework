# Поменять значения местами. Создайте переменные:
#- var_1 = 37
#- var_2 = 99
#-напишите код, который меняет значение переменных местами (var_1 должен быть равен 99 и var_2 — 37)
#- выведите обновленные переменные на экран

#1 способ: с помощью временной переменной,сохраняем в нее значение первой переменной:

var_1 = 37
var_2 = 99

temporary_variable = var_1
var_1 = var_2
var_2 = temporary_variable

print('var_1 =', var_1)
print('var_2 =', var_2)

#2 способ: арифметический:

var_1 = 37
var_2 = 99

var_1 = var_1 + var_2
var_2 = var_1 - var_2
var_1 = var_1 - var_2

print('var_1 =', var_1)
print('var_2 =', var_2)

#3 способ: множественное присваивание (это возможность сразу присвоить несколько значений нескольким переменным):

var_1 = 37
var_2 = 99

var_1, var_2 = var_2, var_1

print('var_1 =', var_1)
print('var_2 =', var_2)

#готово