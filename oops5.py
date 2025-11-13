#Private Variables and Methods
class Car:
    def __init__(self, name, model, year, vin):
        self.name = name
        self.model = model
        self.year = year
        self.__vin = vin

    def display_info(self):
        return f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}"

    def __display_vin(self):  # Private method
        return f"VIN: {self.__vin}"

    #Setter for vin
    def show_vin(self):
        return self.__display_vin()  # Public method to access private method
# Example usage:
my_car = Car("Toyota", "Corolla", 2020, "1HGBH41JXMN109186")
print(my_car.display_info())
print(my_car.show_vin())

# The above code demonstrates the use of private variables and methods in a class.
# The __vin attribute and __display_vin method are private and cannot be accessed directly from outside the class.
# However, the public method show_vin provides a way to access the private method, encapsulating the internal details of the class.