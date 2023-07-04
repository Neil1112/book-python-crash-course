# tuple of five foods
foods = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')

for food in foods:
    print(food)

print("\n")

# try to modify the tuple
# foods[0] = 'burger'     # TypeError: 'tuple' object does not support item assignment

# but we can change the value of a variable that holds a tuple
foods = ('burger', 'fries', 'coke', 'sandwich')

for food in foods:
    print(food)