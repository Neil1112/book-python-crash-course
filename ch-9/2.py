class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is open for business.")


restaurant_0 = Restaurant('Olive Garden', 'Italian')
restaurant_1 = Restaurant('Red Lobster', 'Seafood')
restaurant_2 = Restaurant('Taco Bell', 'Mexican')

print(f"Restaurant name: {restaurant_0.name}")
restaurant_0.describe_restaurant()
print('\n')

print(f"Restaurant name: {restaurant_1.name}")
restaurant_1.describe_restaurant()
print('\n')

print(f"Restaurant name: {restaurant_2.name}")
restaurant_2.describe_restaurant()
print('\n')