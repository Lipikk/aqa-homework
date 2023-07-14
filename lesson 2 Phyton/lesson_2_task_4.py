# Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
# функция должна печатать числа от 1 до n. При этом:
# - если число делится на 3, печатать `Fizz`;
# - если число делится на 5, печатать `Buzz`;
# - если число делится на 3 и на 5, печатать `FizzBuzz`


n = int(input("Введите число от 1 до n: "))

def fizz_buzz(n):
     for n in range(1, n):
      if (n % 3 == 0) and (n % 5 == 0):
         print("FizzBuzz")
      elif (n % 3 == 0):
         print("Fizz")
      elif (n % 5 == 0):
         print("Buzz")
      else:
         print(n) 

fizz_buzz(n)


