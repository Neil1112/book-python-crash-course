class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting.")

    def roll_over(self):
        print(f"{self.name} is rolling over.")

my_dog = Dog('Willie', 6)

# Accessing attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling methods
my_dog.sit()
my_dog.roll_over()

print('\n')

# working with classes and instances
class Car:
    def __init__(self, make, model, year):
        # initialize attributes
        self.make = make
        self.model = model
        self.year = year
        # setting a default value for an attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # set the odometer reading to the given value
        # reject the change if it attempts to roll the odometer back
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        # add the given amount to the odometer reading
        # reject negative values
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23_500)
my_new_car.read_odometer()
my_new_car.update_odometer(23_000)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_new_car.increment_odometer(-100)
my_new_car.read_odometer()


print('\n')

# importing classes
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23_500)
my_new_car.read_odometer()
my_new_car.update_odometer(23_000)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_new_car.increment_odometer(-100)
my_new_car.read_odometer()

print('\n')

# importing multiple classes
from car import Car, ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2019)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

print('\n')


# python standard library
from random import randint, choice

print(randint(1, 6))
print(choice(['apple', 'banana', 'cherry', 'durian', 'eggplant', 'fig']))

print('\n')

