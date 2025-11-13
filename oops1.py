# Defining a Car class to represent a car with attributes and methods
class Car:
    # Constructor to initialize car attributes
    # name, model, and year are the attributes of the Car class and are initialized using the constructor method __init__
    # self is a reference to the current instance of the class
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        
    # Method to display car information
    def display_info(self):
        return f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}" 
    
# Example usage:
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_info())


# Creating another instance of the Car class
another_car = Car("Honda", "Civic", 2019)
print(another_car.display_info())

# The above code defines a Car class with a constructor to initialize its attributes and a method to display the car's information.
# Each instance of the Car class represents a different car with its own name, model, and year.
# The display_info method returns a formatted string containing the car's details.
