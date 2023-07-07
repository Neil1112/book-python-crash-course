class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is open for business.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor}")


ice_cream_stand = IceCreamStand('Baskin Robbins', 'Ice Cream', ['Chocolate', 'Vanilla', 'Strawberry'])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()