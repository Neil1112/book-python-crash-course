from pathlib import Path

path = Path('guest.txt')

names = ''

while True:
    print("Enter 'q' to quit.")
    name = input("What's your name? ")
    if name == 'q':
        break
    else:
        names += name + '\n'

    
path.write_text(names)
print("Guests' names have been saved to the file.")
