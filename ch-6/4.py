glossary = {
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'An immutable list.',
    'if-elif-else': 'A conditional statement.',
    'for': 'A loop statement.',
}

for key, value in glossary.items():
    print(f"{key.title()}: {value}")

print('\n')

# adding new key-value pairs
glossary['while'] = 'Another loop statement.'
glossary['set'] = 'A collection in which each item must be unique.'
glossary['print'] = 'A function to display output.'
glossary['variable'] = 'A placeholder for a value.'
glossary['string'] = 'A series of characters.'
glossary['integer'] = 'A whole number.'
glossary['float'] = 'A decimal number.'
glossary['boolean'] = 'A value of either True or False.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'

for key, value in glossary.items():
    print(f"{key.title()}: {value}")
