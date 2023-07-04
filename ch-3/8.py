places = ["New York", "Rome", "London", "Tokyo", "Paris"]

print("Original list:")
print(places)

print("\nSorted list:")
print(sorted(places))

print("\nOriginal list:")
print(places)               # list is still in original order

print("\nReversed list:")
print(sorted(places, reverse=True))

print("\nOriginal list:")
print(places)               # list is still in original order


# change the chronological order of the list
print("\nReversed Chronological list:")
places.reverse()            # does not returns a list
print(places)

# change the chronological order of the list again
print("\nChronological list:")
places.reverse()            # does not returns a list
print(places)


# sort the list permanently
print("\nSorted list:")
places.sort()
print(places)

print("\nOriginal list:")
print(places)

# sort the list permanently in reverse order
print("\nReverse Sorted list:")
places.sort(reverse=True)
print(places)

print("\nOriginal list:")
print(places)