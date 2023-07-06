def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks

    return album




print(make_album('eminem', 'recovery'))
print(make_album('akon', 'freedom'))
print(make_album('pitbull', 'planet pit'))
print(make_album('eminem', 'recovery', 17))
