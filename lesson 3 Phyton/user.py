# Создание класса

class User:
    first_name = "Ivan"
    last_name = "Ivanov" 

    def __init__(self):
        print("Я создался")

    def printName(self):
        print(self.first_name)

    def printSurname(self):
        print(self.last_name)

    def printNameSurname(self):
        print(self.first_name, self.last_name)



class A(object):
    # func: A user-defined function object
    #
    # Note that func is a function object when it's defined,
    # and an unbound method object when it's retrieved.
    def func(self): 
        pass

    # classMethod: A class method
    @classmethod
    def classMethod(self):
        pass

class B(object):
    unboundMeth = A.func

a = A()
b = B()

print A.func

print a.func

print B.unboundMeth

print b.unboundMeth

print A.classMethod

print a.classMethod






