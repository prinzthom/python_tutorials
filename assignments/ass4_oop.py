class Vehicle:
    def __init__(self,name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return  self.capacity*100

class Bus(Vehicle):
    def __init__(self,name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage, capacity)

    def fare(self):
        cost_per_vehicle = self.capacity * 100
        ten_percent = cost_per_vehicle * 10/100
        return cost_per_vehicle + ten_percent

schoolbus=Bus("school volvo",80,12,50)
print(f"school bus fare is:{schoolbus.fare()}")