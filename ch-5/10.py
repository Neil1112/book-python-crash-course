current_users = ['admin', 'John', 'Mary', 'Jane', 'Mark']

new_users = ['admin', 'John', 'Mary', 'Luke', 'Paul', 'Peter']

# Make a copy of current_users and convert it to lowercase
lower_current_users = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in lower_current_users:
        print("You need to enter a new username")

    else:
        print("username is available")

        