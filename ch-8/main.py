# defining a function
def greet(name):
    print("Hello, " + name + ". Good morning!")

greet('John')


print('\n')


# positional arguments
# positional arguments are passed to a function in the order they are given
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

print('\n')


# keyword arguments
# keyword arguments are name-value pairs that you pass to a function
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


print('\n')

# optinal arguments
# optional arguments are arguments that are given a default value
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print('\n')


# modifying a list in a function
# when you pass a list to a function, the function can modify the list
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print('\n')

# preventing a function from modifying a list
# to keep the original list intact, you can send a copy of the list to the function
# the slice notation [:] makes a copy of the list to send to the function
print_models(unprinted_designs[:], completed_models)

print('\n')

# arbitrary number of arguments
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print('\n')

# mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')

# using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

print('\n')


# storing your functions in modules
# a module is a file ending in .py that contains the code you want to import into your program
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')


# importing specific functions
# syntax: from module_name import function_0, function_1, function_2
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')


# using as to give a function an alias
# syntax: from module_name import function_name as fn
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')


# using as to give a module an alias
# syntax: import module_name as mn
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')





