# importing an entire module
import pizza
print('Importing an entire module:')
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')

# importing specific functions
import pizza as p
print('Importing specific functions:')
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')

# using as to give a function an alias
print('Using as to give a function an alias:')
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')

# using as to give a module an alias
from pizza import make_pizza as mp
print('Using as to give a module an alias:')
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')

# importing an entire module
import pizza as p
print('Importing an entire module:')
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')

# importing all functions in a module
from pizza import *
print('Importing all functions in a module:')
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')