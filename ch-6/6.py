friends = ['jen', 'sarah', 'edward', 'phil', 'james', 'john', 'jane', 'jessica', 'julie', 'jacob']

favourite_languages = {
    'jen': 'python',
    'james': 'c',
    'jane': 'ruby',
    'jacob': 'python',
}

for friend in friends:
    if friend in favourite_languages.keys():
        print(f"{friend.title()}, thank you for taking the poll.")
    else:
        print(f"{friend.title()}, please take the poll.")