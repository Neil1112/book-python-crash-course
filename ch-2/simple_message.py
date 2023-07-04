message = "Hello World"

print(message)

message = "Hello Python Crash Course World!"

print(message)



# on strings, the title method changes the first letter of each word to uppercase
name = "ada lovelace"
print(name.title())

# other useful string methods
print(name.upper())
print(name.lower())


# using a variable inside string
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)


# removing extra space from a string from right side
favorite_language = 'python '
print(favorite_language)

favorite_language = favorite_language.rstrip()
print(favorite_language)

# removing extra space from a string from both sides
favorite_language = ' python '
print(favorite_language)

favorite_language = favorite_language.strip()
print(favorite_language)


# removing prefixes
url = 'https://www.python.org'
url = url.removeprefix('https://')
print(url)