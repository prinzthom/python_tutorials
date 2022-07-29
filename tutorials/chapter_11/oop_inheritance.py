class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def introduce(self):
        print(f"Hey I am {self.brand} {self.model}. I cost {self.price}$")

class SmartPhone(Phone):
    def __init__(self, brand, model, price, ram, storage, camera):
        super().__init__(brand, model, price)
        self.ram = ram
        self.storage = storage
        self.camera = camera

s1 = SmartPhone("Apple", "Iphone 13 pro max", 1700, "8gb", "2tb", "128px")
s1.introduce()