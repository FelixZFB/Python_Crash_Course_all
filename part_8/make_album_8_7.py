# coding=utf-8
# 详细说明见书P125

# 返回值为字典
def make_album(singer, album, number = ''):
    """return to album's information"""
    full_album = {'singer': singer, 'album': album}
    if number:
        full_album['number'] = number
    return full_album

musician = make_album('Felix', 'Love')
print(musician)

musician = make_album('Felix', 'Love', 28)
print(musician)

musician = make_album('Felix', 'Love', number = '28')
print(musician)


