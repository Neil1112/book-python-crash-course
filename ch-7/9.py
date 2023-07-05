sandwiches = ['veg', 'pastrami', 'cheese', 'pastrami', 'coleslaw', 'mexican', 'pastrami', 'tandoori']

print('The deli has run out of pastrami.')

while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')

print('\nSandwiches made:')
for sandwich in sandwiches:
    print(f'\t{sandwich}')

