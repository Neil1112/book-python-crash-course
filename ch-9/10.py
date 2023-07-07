from restaurant import Restaurant

restaurant = Restaurant("The Cheesecake Factory", "American")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"Number served: {restaurant.number_served}")
restaurant.number_served = 10
print(f"Number served: {restaurant.number_served}")
restaurant.set_number_served(20)
print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(30)
print(f"Number served: {restaurant.number_served}")
