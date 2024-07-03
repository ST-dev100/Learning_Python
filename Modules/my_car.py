from car import Car,ElectricCar

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car)
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'roadster', 2019)

