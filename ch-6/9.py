favourite_places = {
    'john': ['paris', 'london', 'new york'],
    'jane': ['tokyo', 'rome', 'berlin'],
    'jack': ['moscow', 'madrid', 'amsterdam'],
}

for name, places in favourite_places.items():
    print(f"{name.title()}'s favourite places are:")
    for place in places:
        print(f"\t{place.title()}")