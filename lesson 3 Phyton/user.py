# Создание класса

class User():
    """в классе 3 метода которые печатают имя, фамилию и имя + фамилия """
    pass

    def __init__(self, first_name, last_name):
        """свойства юзера """
        self.first_name = first_name
        self.last_name = last_name 
    
    def getName(self):
        print(self.first_name)
        
    def getSurname(self):
        print(self.last_name)
    
    def getPersonalInformation(self):
        print(self.first_name, self.last_name)
    

name1 = User("Eлена", "Мурзина")
name2 = User("Elena", "Murzina")

#print(name1.first_name)
#print(name1.last_name)

name1.getName()
name1.getSurname()
name1.getPersonalInformation()

name2.getName()
name2.getSurname()
name2.getPersonalInformation()

    


