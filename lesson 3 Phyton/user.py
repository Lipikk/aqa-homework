# Создание класса

class User:
    pass

    def __init__(self,first_name, last_name):
        self.Name = first_name
        self.Surname = last_name  
    
    def getName(self):
        return self.Name
        
    def getSurname(self):
        return self.Surname
    
    def getPersonalInformation(self):
        return self.Name, self.Surname

person = User("Елена", "Mурзина")




    


