class Car:
    def __init__(self,money):
        self.money = money
    def display(self):
        print(self.money)
        return "j"

car1 = Car(300)

print(car1.display())

class ElectricCar(Car):
    def __init__(self,money,kilometer):
        super().__init__(money)
        self.kilometer = kilometer
    def kil(self):
        print(self.kilometer)

elecricCar = ElectricCar(12,9)   
print(elecricCar.kil())

