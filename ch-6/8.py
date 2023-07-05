pet_0 = {
    'name': 'doggo',
    'kind': 'dog',
    'owner': 'john',
}

pet_1 = {
    'name': 'catto',
    'kind': 'cat',
    'owner': 'jane',
}

pet_2 = {
    'name': 'birb',
    'kind': 'bird',
    'owner': 'jack',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"Name: {pet['name'].title()}")
    print(f"Kind: {pet['kind'].title()}")
    print(f"Owner: {pet['owner'].title()}\n")