name = 'John'

if name == 'John':
    print('Hello John')


# test using lower
if name.lower() == 'john':
    print('Hello John')


# numerical tests with equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
age = 18
if age == 18:
    print('You are 18 years old')

grade = 80

if grade >= 80:
    print('Excellent')

if grade < 40:
    print('You have failed the exam')


# test using and
if age >= 18 and grade >= 80:
    print('You are an adult and you have an excellent grade')


# test whether an item is in list
fruits = ['apple', 'banana', 'orange']

if 'orange' in fruits:
    print('Orange is in the list')

if 'strawberry' not in fruits:
    print('Strawberry is not in the list')