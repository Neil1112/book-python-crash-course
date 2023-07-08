# reading from a file
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text().rstrip()

# accessing file's lines
lines = contents.splitlines()

for line in lines:
    print(line)


# working with file's contents
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

print(pi_string)


