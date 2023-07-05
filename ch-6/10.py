favourite_numbers = {
    'john': [1, 2, 3],
    'jane': [4, 5, 6],
    'jack': [7, 8, 9],
    'jill': [10, 11, 12],
    'james': [13, 14, 15],
}

for name, numbers in favourite_numbers.items():
    print(f"{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{number}")