# multiple line prompt in inpt() function
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

print('\n')

# integer input
age = input("How old are you? ")
age = int(age)
print(age >= 18)

print('\n')

# letting user choose when to quit
prompt = "\nTell me something, and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)


# using a flag variable
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# using break to exit a loop
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f'I\'d love to go to {city.title()}!')

print('\n')

# moving items from one list to another
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed:')

for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

print('\n')

