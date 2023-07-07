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


restaurant = Restaurant('Olive Garden', 'Italian')

print(f"Restaurant name: {restaurant.name}")
print(f"Cuisine type: {restaurant.type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"Number served: {restaurant.number_served}")
restaurant.number_served = 10
print(f"Number served: {restaurant.number_served}")
restaurant.set_number_served(20)
print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(30)
print(f"Number served: {restaurant.number_served}")


