# Банковское приложение: пользователь делает вклад в размере Х рублей сроком на Y лет под 10% годовых 
#(каждый год размер его вклада увеличивается на 10%, эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты)

def bank():
    stavka = 0.1
    x = int(input("На какую сумму вклад?""\n""-> "))
    y = int(input("На какой срок вклад?""\n""-> "))

    
    x = x*(1+stavka)**y
    print("Получите в конце срока", x, "рублей")
bank()

# задание со * 