class Laptop:
    def __init__(self,brand,model,price,processor,ram,storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.processor = processor
        self.ram = ram
        self.storage = storage
    
    def specs(self):
        print(f"Laptop: {self.brand} {self.model}       storage:{self.storage} RAM:{self.ram} processor:{self.processor}")


l1 = Laptop("apple", "m1 macbook pro", 2200, "m1", "16gb", "512gb")
l2 = Laptop("dell", "xps 15 plus", 2000, "intel core i9", "32gb", "512gb")

l1.specs()
l2.specs()