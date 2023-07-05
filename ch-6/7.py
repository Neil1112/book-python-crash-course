person_0 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',
}
person_1 = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 25,
    'city': 'New York',
}
person_2 = {
    'first_name': 'Jack',
    'last_name': 'Doe',
    'age': 20,
    'city': 'New York',
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")
    