sandwiches = ['veg', 'cheese', 'coleslaw', 'mexican', 'tandoori']
finished_sandwiches = []

while sandwiches:
    sandwich = sandwiches.pop()
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)

print('\nSandwiches made:')
for sandwich in finished_sandwiches:
    print(f'\t{sandwich}')
