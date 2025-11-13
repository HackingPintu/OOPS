#Abstraction

class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
def animal_sound(animal):
    print(animal.make_sound())

# Example usage:
dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)
# The above code demonstrates abstraction by defining an abstract class Animal with a method make_sound.
# The Dog and Cat classes inherit from Animal and provide their own implementations of the make_sound method. allowing for different behaviors based on the object type passed in.
# This showcases polymorphism, as the same function can operate on different types of objects. allowing for different behaviors based on the object type passed in.
# This showcases polymorphism, as the same function can operate on different types of objects. allowing for different behaviors based on the object type passed in.
# This showcases polymorphism, as the same function can operate on different types of objects.