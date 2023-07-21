class Smartphone():
    catalog = []

    def __init__(self, phone_brand, phone_model, subscriber_number):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.subscriber_number = subscriber_number

smartphone1 = Smartphone("samsung", "gallaxy", "+79600030303")
smartphone2 = Smartphone("apple", "13pro", "+79176665544")
smartphone3 = Smartphone("xiaomi", "redmi12", "+79375554433")
smartphone4 = Smartphone("HONOR", "70", "+79371111111")
smartphone5 = Smartphone("Poco", "M5", "+79375551122")


#print("phone_brand", "-", "phone_model", ".", 'subscriber_number')

