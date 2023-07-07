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


class Battery:
    def __init__(self, battery_size=40):
        # initialize the battery's attributes
        self.battery_size = battery_size

    def describe_battery(self):
        # print a statement describing the battery size
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        # print a statement about the range this battery provides
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        # initialize attributes of the parent class
        super().__init__(make, model, year)
        # initialize attributes specific to an electric car
        self.battery = Battery()

    def fill_gas_tank(self):
        # electric cars don't have gas tanks
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
print('Upgrading battery...')
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()