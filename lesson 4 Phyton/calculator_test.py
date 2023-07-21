from calculator import Calculator

calculator = Calculator() 



#проверяем сложение ++ чисел
#проверяем сложение -- чисел
#проверяем сложение -+
#проверяем сложение чисел с ..
#проверяем сложение любое число + 0 (n 0)

print('start')
res = calculator.sum(4,5)
assert res == 10
print('finish')