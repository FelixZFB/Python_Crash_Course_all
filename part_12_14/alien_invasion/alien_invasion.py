# -*- coding: cp936 -*-
# 创建一个空的Pygame窗口

import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    
    # 初始化游戏,设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一个Play按钮，由于游戏开始前创建，放在最前面
    play_button = Button(ai_settings, screen, "PLAY")
    
    # 创建一艘飞船的实例,ship就是屏幕上创建的一艘飞船，
    # ship是一个实例的名称，该ship与模块ship的名称无关
    ship = Ship(ai_settings, screen)
    
    # 创建一个用于存储子弹的编组，Group类，类似于列表，用于添加每一颗子弹，用于后期的管理
    bullets = Group()
    
    # 创建一个外星人编组,用于添加每一个外星人
    aliens = Group()
    
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # 创建一个用于存储游戏统计信息的实例,并创建计分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # 开始游戏的主循环
    while True:
        
        # 检查玩家的输入，监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
            aliens, bullets)
        
        # 游戏处于活动状态时，执行以下程序，飞船用完，游戏就停止不动了
        if stats.game_active:
            
            # 更新飞船的位置
            ship.update() #调用ship实例中的方法update,ship是一个实例，而不是ship模块
            
            # 更新所有未消失子弹的位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, 
                bullets)
            
            # 更新外星人的位置
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
        
        # 使用更新后的飞船和子弹位置重新绘制屏幕，更新屏幕上的图像，并切换到新屏幕
        # 绘制屏幕要放在循环的最后，上面所有的代码执行一遍，为绘制屏幕提供了所有的信息
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, 
            bullets, play_button)

        
run_game()
