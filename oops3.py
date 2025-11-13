#Inheritance

class Animal:
    def speak(self):
        return "Animal sound"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
def animal_sound(animal):
    print(animal.speak())

# Example usage:
dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)
# The above code demonstrates inheritance by defining a base class Animal with a method speak.
# The Dog and Cat classes inherit from Animal and override the speak method to provide specific sounds for each animal type.
# The animal_sound function takes an Animal object as an argument and calls its speak method, showcasing polymorphism.