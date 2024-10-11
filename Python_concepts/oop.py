#OOP - Object Oriented Programming
#programming paradigm that organizes code around objects

#Key Concepts
#Class, Object, Atrributes, Methods

#Pillars of OOP
#Encapsulation, Abstraction, Inheritance, Polymorphism

# print("""Four Pillars of OOP:
# Encapsulation: Bundling the data (attributes) and methods (functions) into a single unit (class) and restricting access to some of the object's components.
# Abstraction: Hiding the complex implementation details and exposing only the necessary parts.
# Inheritance: One class can inherit properties and methods from another class, promoting code reusability.
# Polymorphism: Different objects can be treated as instances of the same class through a common interface, allowing different implementations for the same method name.""")

#A Class
class Study_Degree:
    #constructor method
    def __init__(self,name,year,institution):
        self.name=name
        self.year=year
        self.institution = institution

    #Method to display the class details
    def display_info(self):
        print(f"Study Degree: {self.name} {self.year} {self.institution}")


#create a object(instance) of the class
student1 = Study_Degree("Red",2024,"Cambridge")

#accessing the object's attributes
print(student1.name) #output is the name of the student

#calling the object's method
student1.display_info()

#Encapsulation
#making attributes private and accessing them using getter and setter methods
class Person:
    print("Encapsulation Example")
    def __init__(self, name, age):
        self._name = name #protected attribute
        self.__age = age #private attribute

        #getter method for private attribute
    def get_age(self):
        return self.__age
        
        #setter method for private attribute
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")

person1 = Person("Red",34)
print(person1.get_age())
person1.set_age(24)
print(person1.get_age())

#Inheritance
#allows a class to inherit other available attributes and methods from another class

#Base Class       (Parent)
class Company:
    print("Inheritance Example")
    def __init__(self, name):
        self.name = name 
    
    def product(self):
        print(f"{self.name} creates products.")

#derived class which inherits from Company Class (Child)
class Search_engine(Company):
    def product(self):
        print(f"{self.name} built search engines.")

#another derived class
class Phone(Company):
    def product(self):
        print(f"{self.name} creates smartphone and laptops.")

google = Search_engine("Google")
microsoft = Search_engine("Microsoft")
samsung = Phone("Samsung")
apple = Phone("Apple")

google.product()
apple.product()
samsung.product()
microsoft.product()

#polymorphism
#allows different types of objects to be treated under a common superclass

class Shape:
    print("Polymorphism example")
    def area(self):
        pass #abstract method

#derived classes
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
shapes = [Circle(4), Rectangle(7,6)]
for shape in shapes:
    print(shape.area())

#Abstraction
#concept of hiding internal details of how it works
#showing only necessary parts
#often implemented using abstract base classes(ABC)
from abc import ABC, abstractmethod

#Abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine....")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Starting motorcycle engine...")

#Abstraction in action
vehicles = [Car(), Motorcycle()]

for vehicle in vehicles:
    vehicle.start_engine()

# Instance attributes: Defined inside the constructor (__init__), unique to each object.
# Class attributes: Defined outside the constructor, shared among all instances of the class.

#Dunder Methods
#Customization for builtin behaviour
#__init__
#__str__
#__repr__
#__len__