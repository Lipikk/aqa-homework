# Создание класса

class User:
    def __init__(self, first_name, last_name ):
        print("Я создался")
        self.first_name = first_name
        self.last_name = last_name

    def printName(self):
        print(self.first_name)

    def printSurname(self):
        print(self.last_name)

    def printNameSurname(self):
        print(self.first_name, self.last_name)







