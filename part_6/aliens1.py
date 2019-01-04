# coding=utf-8
# 目的：列表中存储字典，同时修改外星人的颜色

# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色外星人
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 修改前三个外星人的颜色
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 显示前5个外星人，看前3个是否已经修改
for alien in aliens[0:5]:
    print(alien)
print("...")

# 继续扩展这个循环，将前3个机器人修改为红色
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:5]:
    print(alien)
print("...")
        





