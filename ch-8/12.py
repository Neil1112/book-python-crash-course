def make_sandwich(*args):
    for arg in args:
        print(f"Making a {arg} sandwich.")

make_sandwich('cheese')
print('\n')
make_sandwich('cheese', 'tomato')
print('\n')
make_sandwich('cheese', 'tomato', 'coleslaw')