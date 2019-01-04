favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

names = ['sarah', 'felix','phil']
for name in names:
    if name in favorite_languages.keys():
        print(name.title() + ", thank you for your participation")
    else:
        print(name.title() + ", we want to invite you for survey")
