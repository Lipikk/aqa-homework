# Приведение типов:

#1 часть Создать переменную my_age через функцию input и вывести на экран сообщение в формате «Ваш возраст: my_age»

#my_age = input("Укажите ваш возраст?")
#print("Ваш возраст:" + my_age)


#2 часть:Сохранить в переменную my_age = my_age + 1, преобразовать значение my_age к типу «число» и перезапустить скрипт

#my_age = input("my_age: ")
#print("Ваш возраст:" + my_age)
#my_age_new = int(my_age)
#print("Ваш обновленный возраст:", my_age_new + 1)

my_age = int(input("my_age: "))
print(f'my_age:{my_age}')
my_age = my_age + 1
print(f'my_age:{my_age}')
my_age += 1
print(f'my_age:{my_age}')
