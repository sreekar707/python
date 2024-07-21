class Car:
    Total_Car=0
    def __init__(self,brand,model,price):
        self.brand= brand
        self.model= model
        self.price=price
        Car.Total_Car+=1


    def full_name (self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "petrol or diesel"

    @staticmethod
    def general_description():
        return "cars are means of transport"


my_car=Car("tata","safari","30000")
Car("tata","safari","3000000")
print(my_car.general_description())
print(Car.general_description())



class ElectricCar(Car):
    def __init__(self,brand,model,price,battery_size):
        super ().__init__(brand,model,price,)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"

my_tesla=ElectricCar("tesla","models","30000","85kws")
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))
# # print(my_tesla.full_name())

# print(my_tesla.fuel_type())


# safari=Car("tata","safari","60000")
# Nexon=Car("tata","nexon","400000")
# Tigor=Car("tata","tigor","80000")
# print(safari.fuel_type())
# print(Car.Total_Car)
# my_car=Car("toyota","corolla","10000")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.price)


# print(my_car.full_name())

# my_new_car=Car("tata","tiago","20000")
# print(my_new_car.brand)

