prompt = '\nTell us your age and we will tell you the price of your ticket. '
prompt += '\nEnter -1 to exit: '

while True:
    age = input(prompt)
    age = int(age)

    if age == -1:
        break
    elif age < 3:
        print('Your ticket is free.')
    elif age >= 3 and age <= 12:
        print('Your ticket is $10.')
    elif age > 12:
        print('Your ticket is $15.')
    else:
        print('Invalid input.')
