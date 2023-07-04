guests = ["Newton", "Turing", "Einstein"]

# guests[2] can't make it
guests.pop(2)

# invite Hawking instead
guests.append("Hawking")

# greet people for dinner
print(f"Hello {guests[0]}, would you like to have dinner with me?")
print(f"Hello {guests[1]}, would you like to have dinner with me?")
print(f"Hello {guests[2]}, would you like to have dinner with me?")