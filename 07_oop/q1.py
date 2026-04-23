class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    def gen_desc(self):
        return 'Cars are amazing'


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar('Tesla', 'Model S', '85kwh')

# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))

print(my_tesla.fuel_type())

my_car = Car('Toyota', 'Corolla')
print(my_car.fuel_type())

my_new_car = Car('Mercedes', 'AMG')
print(my_new_car.get_brand(), my_new_car.model)

print(my_tesla.total_car)


class Battery:
    def battery_info(self):
        return 'this is battery'

class Engine:
    def engine_info(self):
        return 'this is engine'

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCarTwo('Tesla', 'Model Y')
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
