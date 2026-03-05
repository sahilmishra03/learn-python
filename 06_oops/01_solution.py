class Car:
    car_count=0
    def __init__(self):
        Car.car_count=Car.car_count+1
    def set_brand(self,brand):
        self.__brand=brand
    def set_fuelTyepe(self,fuelType):
        self.__fuelType=fuelType
    def nameOfCar(self):
        print(self.__brand+" "+self.model) 
    def get_brand(self):
        return self.__brand
    def fuelTyepe(self):
        print("Petrol")

    @staticmethod
    def carDescription():
        return "Car is used for travelling"

# class ElectricCar(Car):
#     def __init__(self,brand,model,batterySize):
#         self.brand=brand
#         self.__model=model
#         self.batterySize=batterySize
#     def fuelTyepe(self):
#         print("Electric")
#     @property
#     def model(self):
#         return self.__model
        
# tesla = ElectricCar("Tesla","S","85kwh")
# print(isinstance(tesla,Car))
# print(isinstance(tesla,ElectricCar))
# tesla.model="Nexon"
# print(tesla.model)
# tesla.fuelTyepe()

# safari = Car()
# safari.model="Nexon"
# print(safari.model)
# newCar = Car("Hyundai","Creata")
# print(newCar.model)
# print(newCar.brand)
# newCar.nameOfCar()

# newCar2 = Car("Toyota","Fortuner")
# print(newCar2.model)
# print(newCar2.brand)
# newCar2.nameOfCar()

class Car:
    def __init__(self):
        print("This is a Car class")

class Battery:
    def __init__(self):
        print("This is a Battery class")

class Engine:
    def __init__(self):
        print("This is a Engine class")

class ElectricCar(Battery, Engine, Car):
    def __init__(self):
        super().__init__()
        print("This is a Electric Car class")

tesla = ElectricCar()