# checking whether a value is in list
requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)


# checking whether a value is not in list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


# if-elif-else chain
age = 12
if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $25.')
else:
    print('Your admission cost is $40.')


# consise if-elif-else chain
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f'Your admission cost is ${price}.')


# omitting the else and using elif for clarity
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 18:
    price = 40

print(f'Your admission cost is ${price}.')


# testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')

print('\n')

# using multiple lists and if statements
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print('\nFinished making your pizza!')