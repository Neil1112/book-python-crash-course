# accessing value from dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

# adding new key-value pair
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# more interesting example
alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien['x_position']}")

if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien['x_position'] += x_increment

print(f"New position: {alien['x_position']}")

# removing key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# dictionary of similar objects
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(f"Sarah's favourite language is {favourite_languages['sarah'].title()}.")


# looping through all key-value pairs
user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# looping through all the keys
for key in user.keys():
    print(key.title())

# looping through keys in a particular order
for key in sorted(user.keys()):
    print(key.title())

# looping through all values
for value in favourite_languages.values():
    print(value.title())

# looping through all unique values
for value in set(favourite_languages.values()):
    print(value.title())

print('\n')

# list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('\n')

# dictonaries in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'age': 76,
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'age': 66,
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    print(f"Full name: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"Location: {user_info['location'].title()}")
    print(f"Age: {user_info['age']}")