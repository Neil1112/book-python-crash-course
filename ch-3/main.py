bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# string methods on elements of list
print(bicycles[0].title())

# last element of list
print(bicycles[-1])

# changing element of list
bicycles[0] = 'honda'
print(bicycles)

# appending element to list
bicycles.append('trek')
print(bicycles)

# creating an empty list and then appending the values
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# inserting element at a particular index
motorcycles.insert(1, 'ducati')
print(motorcycles)

# removing element from list with del statement
del motorcycles[0]
print(motorcycles)


# removing element from list with pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# popping items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
yamaha = motorcycles.pop(1)
print(f"The motorcycle I owned was a {yamaha.title()}.")


# sorting list permanently with sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sorting list permanently in reverse order
cars.sort(reverse=True)
print(cars)

# sorting list temporarily with sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))

# reversing the order of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
