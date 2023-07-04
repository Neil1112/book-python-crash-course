magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!\n")


# numerical lists

# Using the range() function

for value in range(1, 5):
    print(value)

print("\n")

# range() with just 1 argument
for value in range(6):
    print(value)            # prints 0 to 5

print("\n")

# using range to create a list of numbers
numbers = list(range(1, 6))     # creates a list of numbers from 1 to 5
print(numbers)

print("\n")

# using range() to skip numbers
even_numbers = list(range(2, 11, 2))     # creates a list of even numbers from 2 to 10
print(even_numbers)

print("\n")


# using range() to create a list of squares
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

print("\n")



# Simple statistics with a list of numbers
digits = list(range(0, 10))
print(f"Min: {min(digits)} \n")
print(f"Max: {max(digits)} \n")
print(f"Sum: {sum(digits)} \n")


# List Comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)

print("\n")


# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])        # prints last 3 elements of the list

print("\n")


# looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\n")


# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]      # copies the list
print(friend_foods)

print("\n")

