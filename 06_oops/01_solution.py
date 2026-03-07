# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# my_car = Car("Tata","Safari")
# print(my_car.brand)
# print(my_car.model)

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def fullName(self):
#         return self.brand+"-"+self.model

# my_car = Car("Tata","Safari")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def fullName(self):
#         return self.brand+"-"+self.model
    
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size

# my_electric_car=ElectricCar("Tesla","S Model","85kWh")
# print(my_electric_car.brand)
# print(my_electric_car.model)
# print(my_electric_car.battery_size)
# print(my_electric_car.fullName())

# my_car = Car("Tata","Safari")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())

# class Car:
#     def __init__(self,brand,model):
#         self.__brand=brand
#         self.model=model
#     def fullName(self):
#         return self.brand+"-"+self.model
#     def get_brand(self):
#         return self.__brand
    
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size

# # my_electric_car=ElectricCar("Tesla","S Model","85kWh")
# # print(my_electric_car.brand)
# # print(my_electric_car.model)
# # print(my_electric_car.battery_size)
# # print(my_electric_car.fullName())

# my_car = Car("Tata","Safari")
# # print(my_car.brand)
# print(my_car.model)
# print(my_car.get_brand())

# class Car:
#     def __init__(self,model):
#         self.model=model
#     def fullName(self):
#         return self.brand+"-"+self.model
#     def get_brand(self):
#         return self.__brand
#     def set_brand(self,brand):
#         self.__brand=brand
    
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size

# # my_electric_car=ElectricCar("Tesla","S Model","85kWh")
# # print(my_electric_car.brand)
# # print(my_electric_car.model)
# # print(my_electric_car.battery_size)
# # print(my_electric_car.fullName())

# my_car = Car("S Model")
# # print(my_car.brand)
# print(my_car.model)
# my_car.set_brand("Tesla")
# print(my_car.get_brand())

# class Car:
#     def __init__(self,brand,model):
#         self.__brand=brand
#         self.model=model
#     def fullName(self):
#         return self.brand+"-"+self.model
#     def get_brand(self):
#         return self.__brand
#     def fuelType(self):
#         return "Petrol-Diease"
    
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size
#     def fuelType(self):
#         return "Electic"

# my_electric_car=ElectricCar("Tesla","S Model","85kWh")
# # print(my_electric_car.brand)
# print(my_electric_car.model)
# print(my_electric_car.battery_size)
# # print(my_electric_car.fullName())
# print(my_electric_car.fuelType())


# my_car = Car("Tata","Safari")
# # print(my_car.brand)
# print(my_car.model)
# print(my_car.get_brand())
# print(my_car.fuelType())

# class Car:
#     total_car=0
#     def __init__(self,brand,model):
#         Car.total_car=Car.total_car+1
#         self.__brand=brand
#         self.model=model
#     def fullName(self):
#         return self.brand+"-"+self.model
#     def get_brand(self):
#         return self.__brand
#     def fuelType(self):
#         return "Petrol-Diease"
    
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size
#     def fuelType(self):
#         return "Electic"

# my_electric_car=ElectricCar("Tesla","S Model","85kWh")
# # print(my_electric_car.brand)
# print(my_electric_car.model)
# print(my_electric_car.battery_size)
# # print(my_electric_car.fullName())
# print(my_electric_car.fuelType())


# my_car = Car("Tata","Safari")
# # print(my_car.brand)
# print(my_car.model)
# print(my_car.get_brand())
# print(my_car.fuelType())
# print(my_car.total_car)

# my_car2 = Car("Tata","Nexon")
# # print(my_car.brand)
# print(my_car2.model)
# print(my_car2.get_brand())
# print(my_car2.fuelType())
# print(Car.total_car)

# class Car:
#     total_car=0
#     def __init__(self,brand,model):
#         Car.total_car=Car.total_car+1
#         self.__brand=brand
#         self.model=model
#     def fullName(self):
#         return self.brand+"-"+self.model
#     def get_brand(self):
#         return self.__brand
#     def fuelType(self):
#         return "Petrol-Diease"
#     @staticmethod
#     def general_desc():
#         return "Car Class"
    
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size
#     def fuelType(self):
#         return "Electic"
#     @staticmethod
#     def general_desc():
#         return "Electric Car Class"

# my_electric_car=ElectricCar("Tesla","S Model","85kWh")
# # print(my_electric_car.brand)
# print(my_electric_car.model)
# print(my_electric_car.battery_size)
# # print(my_electric_car.fullName())
# print(my_electric_car.fuelType())


# my_car = Car("Tata","Safari")
# # print(my_car.brand)
# print(my_car.model)
# print(my_car.get_brand())
# print(my_car.fuelType())
# print(my_car.total_car)

# my_car2 = Car("Tata","Nexon")
# # print(my_car.brand)
# print(my_car2.model)
# print(my_car2.get_brand())
# print(my_car2.fuelType())
# print(Car.general_desc())

# class Car:
#     total_car=0
#     def __init__(self,brand,model):
#         Car.total_car=Car.total_car+1
#         self.__brand=brand
#         self.__model=model
#     def fullName(self):
#         return self.__brand+"-"+self.__model
#     def get_brand(self):
#         return self.__brand
#     def fuelType(self):
#         return "Petrol-Diease"
#     @staticmethod
#     def general_desc():
#         return "Car Class"
    
#     @property
#     def model(self):
#         return self.__model
    
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size
#     def fuelType(self):
#         return "Electic"
#     @staticmethod
#     def general_desc():
#         return "Electric Car Class"

# my_electric_car=ElectricCar("Tesla","S Model","85kWh")
# print(my_electric_car.brand)
# print(my_electric_car.model)
# print(my_electric_car.battery_size)
# print(my_electric_car.fullName())
# print(my_electric_car.fuelType())


# my_car = Car("Tata","Safari")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.get_brand())
# print(my_car.fuelType())
# print(my_car.total_car)

# my_car2 = Car("Tata","Nexon")
# my_car2.model="City"
# print(my_car.brand)
# print(my_car2.model)
# print(my_car2.get_brand())
# print(my_car2.fuelType())
# print(Car.general_desc())

# class Car:
#     total_car=0
#     def __init__(self,brand,model):
#         Car.total_car=Car.total_car+1
#         self.__brand=brand
#         self.__model=model
#     def fullName(self):
#         return self.__brand+"-"+self.__model
#     def get_brand(self):
#         return self.__brand
#     def fuelType(self):
#         return "Petrol-Diease"
#     @staticmethod
#     def general_desc():
#         return "Car Class"
    
#     @property
#     def model(self):
#         return self.__model
    
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size
#     def fuelType(self):
#         return "Electic"
#     @staticmethod
#     def general_desc():
#         return "Electric Car Class"

# my_electric_car=ElectricCar("Tesla","S Model","85kWh")
# # print(my_electric_car.brand)
# print(my_electric_car.model)
# print(my_electric_car.battery_size)
# print(my_electric_car.fullName())
# print(my_electric_car.fuelType())


# my_car = Car("Tata","Safari")
# # print(my_car.brand)
# print(my_car.model)
# print(my_car.get_brand())
# print(my_car.fuelType())
# print(my_car.total_car)

# my_car2 = Car("Tata","Nexon")
# # my_car2.model="City"
# # print(my_car.brand)
# print(my_car2.model)
# print(my_car2.get_brand())
# print(my_car2.fuelType())
# print(Car.general_desc())

# print(isinstance(my_car2,Car))
# print(isinstance(my_car,Car))
# print(isinstance(my_electric_car,Car))
# print(isinstance(my_electric_car,ElectricCar))

class Battery:
    def battery_info(self):
        print("Lithium Ions Battery")

class Engine:
    def engine_info(self):
        print("500 HORSE POWER ENGINE")

class ElectricCar(Battery,Engine):
    pass

my_new_Electric_Car=ElectricCar()
my_new_Electric_Car.battery_info()
my_new_Electric_Car.engine_info()