from oops1 import my_car, another_car

print(my_car.display_info())
print(another_car.display_info())

# The above code imports the Car class instances from oops1.py and prints their information using the display_info method.
# This code demonstrates how to reuse class instances defined in another module (oops1.py) by importing them and calling their methods.# Defining a Car class to represent a car with attributes and methods


#Polymorphism Example
class Bike:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        return f"Bike Name: {self.name}, Model: {self.model}, Year: {self.year}"
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        return f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}"
    
def show_vehicle_info(vehicle):
    print(vehicle.display_info())   
    
# Example usage:
my_bike = Bike("Yamaha", "FZ", 2021)
show_vehicle_info(my_bike)
my_car = Car("Toyota", "Corolla", 2020)
show_vehicle_info(my_car)

# The above code demonstrates polymorphism by defining two classes, Bike and Car, each with a display_info method.
# Each class has its own implementation of the display_info method
# The show_vehicle_info function takes an object as an argument and calls its display_info method,