class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is open for business.")


restaurant = Restaurant('Olive Garden', 'Italian')

print(f"Restaurant name: {restaurant.name}")
print(f"Cuisine type: {restaurant.type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()