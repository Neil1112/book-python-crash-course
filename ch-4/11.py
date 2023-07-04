pizzas = ["Margherita", "Farmhouse", "Extravaganza"]

friend_pizza = pizzas[:]

pizzas.append("Peppy Paneer")
friend_pizza.append("Mexican Green Wave")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\n")

print("My friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)

print("\n")

