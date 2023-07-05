prompt = '\nWhich topping would you like to add to your pizza? '
prompt += '\nEnter \'quit\' when you are finished. '

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f'Adding {topping} to your pizza.')

