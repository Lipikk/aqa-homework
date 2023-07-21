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