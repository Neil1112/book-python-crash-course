from random import choice

ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
my_ticket = [1, 2, 3, 4]
counter = 0

while True:

    while len(winning_ticket) < 4:
        pulled_item = choice(ticket)

        if pulled_item not in winning_ticket:
            print(f"We pulled a {pulled_item}!")
            winning_ticket.append(pulled_item)

    if my_ticket == winning_ticket:
        print("You won!")
        break
    else:
        print("Sorry, keep trying.")
        winning_ticket = []
        counter += 1

print(f"It took {counter} tries to win.")