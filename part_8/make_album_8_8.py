# coding=utf-8
# 详细说明见书P125

# 返回值为字典
def make_album(singer, album, number = ''):
    """return to album's information"""
    full_album = {'singer': singer, 'album': album}
    if number:
        full_album['number'] = number
    return full_album

while True:
    print("Please tell me something about album:")
    print("(Enter 'q' at any time to quit)")
    
    singer = input("Singer name: ")
    if singer == 'q':
        break
        
    album = input("Album name: ")
    if album == 'q':
        break
        
    number = input("Nmuber: ")
    if number == 'q':
        break    

    full_album = make_album(singer, album, number)
    print(full_album)


