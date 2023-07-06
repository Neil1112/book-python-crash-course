def make_albums(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks

    return album


while True:
    print("Enter 'q' to quit.")
    artist = input("Enter artist name: ")
    if artist == 'q':
        break

    title = input("Enter album title: ")
    if title == 'q':
        break

    print(make_albums(artist, title))

