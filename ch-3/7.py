guests = ["Newton", "Turing", "Einstein"]

# add 3 more people to the list
guests.insert(0, "Hawking")
guests.insert(2, "Feynman")
guests.append("Bohr")

# i can now invite only 2 people
print("I can invite only 2 people for dinner.")

# remove guests
guest = guests.pop()
print(f"Sorry {guest}, I can't invite you for dinner.")

guest = guests.pop()
print(f"Sorry {guest}, I can't invite you for dinner.")

guest = guests.pop()
print(f"Sorry {guest}, I can't invite you for dinner.")

guest = guests.pop()
print(f"Sorry {guest}, I can't invite you for dinner.")

# greet people for dinner
print(f"Hello {guests[0]}, would you like to have dinner with me?")
print(f"Hello {guests[1]}, would you like to have dinner with me?")

# remove remaining guests
del guests[0]
del guests[0]

# print empty list
print(guests)