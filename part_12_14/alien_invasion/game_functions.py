# -*- coding: cp936 -*-
# 所有游戏中的设置都在这里定义

import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets): 
    #按动键盘移动的是实例飞船，要给一个形参飞船，ship是飞船的一个实例
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右一直移动飞船
        ship.moving_right = True  # ship.moving_right是ship实例中的一个属性
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q: # 按键盘q结束游戏
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中，
    # 检查屏幕子弹是否小于设置的子弹数，才能新建,不然按下空格没有任何操作
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    
def check_keyup_events(event, ship):
    """响应松开键盘"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, 
    bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
                
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 形参mouse_x和mouse_y是在这里提取的属性，作为check_play_button方法的实参
            # 方法check_events并不需要使用mouse_x和mouse_y，所以形参里面不需要
            check_play_button(ai_settings, screen, stats, sb, play_button, 
                ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, 
        aliens, bullets, mouse_x, mouse_y):
    """在玩家单击PLAY按钮时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        
        # 隐藏光标
        pygame.mouse.set_visible(False)
        
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        
        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        
        # 创建一群新的外星人，并让飞船居中底部
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


    
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """更新子弹的位置，移除已消失的子弹"""
    # 更新子弹的位置，在主程序中创建了一个用于存储子弹的编组bullets = Group()，
    # update()是bullet模块中的一个方法
    bullets.update() 
    
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中外星人，如果有，就删除相应的子弹和外星人
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
        aliens, bullets)
            
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
        aliens, bullets):
    # 响应子弹和外星人的碰撞
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    # 创建一群新的外星人(该处代码也可以放在update_aliens方法中，对应修改主程序即可，
    # 由于主程序每次都是代码全部循环一次，放在更新子弹或者更新外星人方法里面都可以)
    if len(aliens) == 0:
        # 删除所有的子弹，加快游戏节奏，并新建一群外星人,并提高一个等级
        bullets.empty()
        ai_settings.increase_speed()
        
        # 提高等级
        stats.level += 1
        sb.prep_level()
        
        # 创建一群新的外星人
        create_fleet(ai_settings, screen, ship, aliens)
    
def check_fleet_edges(ai_settings, aliens):
    """有外星人到达屏幕边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1 

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减去1
        stats.ships_left -= 1
        
        # 更新记分牌
        sb.prep_ships()
        
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        
        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
        # 暂停一点游戏时间,外星人和飞船更新完成后将先暂停一会儿，然后再执行更新屏幕的程序
        # 更新屏幕，将重新显示所有的外星人和飞船，游戏再次开始
        sleep(2)
    
    else:
        aliens.empty()
        bullets.empty()
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人到达屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被外星人撞击一样处理
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 只要检测到有一个飞船到达底部，就结束循环，添加break语句
            break

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人处于屏幕边缘，并更新整群外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
          
def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - 
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x # x坐标需要转换成rect的属性，才能用于上面绘制外星人的函数
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number # 循环时第一行行号为0，得到第一行y左边，依次向下创建多行
    aliens.add(alien) # aliens类似于一个列表，用于管理外星人
    
def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少个外星人，外星人间距为外星人的宽带
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width) # 注意：不能在该处直接写alien_width,该处的alien.rect.width是一个已知的值，作为实参传递给alien_width形参
    number_rows = get_number_rows(ai_settings, ship.rect.height, 
                                    alien.rect.height)
    
    # 创建外星人群，第一次循环时行号为0，外星人数量0-5，创建多个外星人，然后第二次循环行号为1，继续。。。
    for row_number in range(number_rows): 
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
    play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    # 绘制飞船
    ship.blitme()
    
    # 绘制外星人，绘制编组中的每个外星人，绘制的位置由元素的属性rect决定
    aliens.draw(screen) 
    
    # 显示得分
    sb.show_score()
    
    # 如果游戏处于非活动状态，就绘制一个PLAY按钮,
    # 为了让PLAY按钮在图像最上面，绘制飞船子弹之后绘制这个按钮
    # 游戏结束后，stats.game_active = False，双否定就是True,屏幕上就画一个PLAY按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
    
def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
