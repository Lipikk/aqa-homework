# Range. Создайте список [ 18, 14, 10, 6, 2 ] с помощью функции range() и выведите его на экран

#1 способ создания списка:
start = 18
end = 0
step = -4
numbers = list(range(start, end, step))
print(numbers)

#2 способ создания списка:
for numbers in range(18, 0, -4):
   print(numbers)


#3 способ:
start = 18
end = 0
step = -4
 
for list in range(start, end, step):
    print(list, end=' ')


# просто вывести элементы из созданного списка с помощью range:
#list = [ 18, 14, 10, 6, 2 ]
#for i in range (0, len(list)):
  #print(list[i])
#for numbers in range(2, 22, 4):


